"""
Tests for for the top-level & “CMS” views
"""

from django.test import TestCase
from django.urls import reverse

from concordia.models import SimplePage

from .utils import CreateTestUsers, JSONAssertMixin


class TopLevelViewTests(JSONAssertMixin, CreateTestUsers, TestCase):
    def test_healthz(self):
        data = self.assertValidJSON(self.client.get("/healthz"))

        for k in (
            "current_time",
            "load_average",
            "debug",
            "database_has_data",
            "application_version",
        ):
            self.assertIn(k, data)

    def test_homepage(self):
        response = self.client.get(reverse("homepage"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_contact_us_get(self):
        response = self.client.get(reverse("contact"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")

    def test_contact_us_with_referrer(self):
        test_http_referrer = "http://foo/bar"

        response = self.client.get(reverse("contact"), HTTP_REFERER=test_http_referrer)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact.html")

        self.assertEqual(
            response.context["form"].initial["referrer"], test_http_referrer
        )

    def test_contact_us_post(self):
        post_data = {
            "email": "nobody@example.com",
            "subject": "Problem found",
            "link": "http://www.loc.gov/nowhere",
            "story": "Houston, we got a problem",
        }

        response = self.client.post(reverse("contact"), post_data)

        self.assertEqual(response.status_code, 302)

    def test_contact_us_post_invalid(self):
        post_data = {
            "email": "nobody@",
            "subject": "Problem found",
            "story": "Houston, we got a problem",
        }

        response = self.client.post(reverse("contact"), post_data)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            {"email": ["Enter a valid email address."]}, response.context["form"].errors
        )

    def test_simple_page(self):
        s = SimplePage.objects.create(
            title="Help Center 123",
            body="not the real body",
            path=reverse("help-center"),
        )

        resp = self.client.get(reverse("help-center"))
        self.assertEqual(200, resp.status_code)
        self.assertEqual(s.title, resp.context["title"])
        self.assertEqual(
            [(reverse("help-center"), s.title)], resp.context["breadcrumbs"]
        )
        self.assertEqual(resp.context["body"], f"<p>{s.body}</p>")

    def test_nested_simple_page(self):
        l1 = SimplePage.objects.create(
            title="Help Center", body="not the real body", path=reverse("help-center")
        )

        l2 = SimplePage.objects.create(
            title="Help Center Welcome Guide",
            body="This is _not_ the real page",
            path=reverse("welcome-guide"),
        )

        resp = self.client.get(reverse("welcome-guide"))
        self.assertEqual(200, resp.status_code)
        self.assertEqual(l2.title, resp.context["title"])
        self.assertEqual(
            resp.context["breadcrumbs"],
            [(reverse("help-center"), l1.title), (reverse("welcome-guide"), l2.title)],
        )
        self.assertHTMLEqual(
            resp.context["body"], f"<p>This is <em>not</em> the real page</p>"
        )
