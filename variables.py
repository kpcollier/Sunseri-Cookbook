from os import environ

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

google_web = dict(
    client_id=environ.get("google_client_id", "1077262490751-g273abg9enar5fk19bdv33t9q8nb3mcr.apps.googleusercontent.com"),
    project_id=environ.get("google_project_id", "restaurantmenuapp-182904"),
    auth_uri=environ.get(
        "google_auth_uri",
        "https://accounts.google.com/o/oauth2/auth"
    ),
    token_uri=environ.get(
        "google_token_uri",
        "https://accounts.google.com/o/oauth2/token"
    ),
    auth_provider_x509_cert_url=environ.get(
        "google_x509",
        "https://www.googleapis.com/oauth2/v1/certs"
    ),
    client_secret=environ.get(
        "google_client_secret",
        "eGhH19ptt7EvuKQ7CrW1x8U3"
    ),
    javascript_origins=[
        "http://localhost:5000"
    ],
    scope='',
    redirect_uris=[
        "https://localhost:5000/callback",
        "http://localhost:5000/callback"
    ]
)

facebook_web = dict(
    app_id=environ.get('facebook_app_id', '122378008450659'),
    app_secret=environ.get(
        'facebook_app_secret',
        '84dd22626ba992bf36d2dcee96eef0b4'
    )
)

main_app = dict(
    secret_key=environ.get('app_secret_key', 'super secret key'),
    debug=environ.get('debug', True)
)
