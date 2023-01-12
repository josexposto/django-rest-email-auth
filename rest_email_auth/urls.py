"""
URL configuration for the ``rest_email_auth`` app.
"""

from django.urls import path, re_path

from rest_email_auth import views


app_name = "rest-email-auth"


urlpatterns = [
    re_path(r"^emails/$", views.EmailListView.as_view(), name="email-list"),
    re_path(
        r"^emails/(?P<pk>[0-9]+)/$",
        views.EmailDetailView.as_view(),
        name="email-detail",
    ),
    re_path(r"^register/$", views.RegistrationView.as_view(), name="register"),
    re_path(
        r"^request-password-reset/$",
        views.PasswordResetRequestView.as_view(),
        name="password-reset-request",
    ),
    re_path(
        r"^resend-verification/$",
        views.ResendVerificationView.as_view(),
        name="resend-verification",
    ),
    re_path(
        r"^reset-password/$",
        views.PasswordResetView.as_view(),
        name="password-reset",
    ),
    re_path(
        r"^verify-email/$",
        views.EmailVerificationView.as_view(),
        name="verify-email",
    ),
]
