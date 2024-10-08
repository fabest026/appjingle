import base64
import json
import requests
import streamlit as st
import asyncio
from httpx_oauth.clients.google import GoogleOAuth2
from streamlit_oauth import OAuth2Component

async def write_authorization_url(client,
                                  redirect_uri):
    authorization_url = await client.get_authorization_url(
        redirect_uri,
        scope=["profile", "email"],
        extras_params={"access_type": "offline"},
    )
    return authorization_url

async def write_access_token(client,
                             redirect_uri,
                             code):
    token = await client.get_access_token(code, redirect_uri)
    return token

async def get_email(client,
                    token):
    user_id, user_email = await client.get_id_email(token)
    return user_id, user_email


def login_with_google():
    client_id = st.secrets["Google_OAuth_Client_ID"]
    client_secret = st.secrets["Google_OAuth_Client_Secret"]
    redirect_uri = st.secrets["Google_OAuth_Redirect_URI"]

    client = GoogleOAuth2(client_id, client_secret)
    authorization_url = asyncio.run(
        write_authorization_url(client=client,
                                redirect_uri=redirect_uri)
    )

    st.session_state["token"] = None
    if ("authentication_status" not in st.session_state or st.session_state["authentication_status"] is None) \
            and st.session_state["token"] is None:
        try:
            code = st.experimental_get_query_params()['code']
        except:
            st.write(f"""<b>
                You can login directly using your <a target="_self"
                href="{authorization_url}">Google Account</a></b><br><br>""",
            unsafe_allow_html=True)
        else:
            # Verify token is correct:
            try:
                token = asyncio.run(
                    write_access_token(client=client,
                                       redirect_uri=redirect_uri,
                                       code=code))
            except:
                st.write(f"""<b>
                You can login directly using your <a target="_self"
                href="{authorization_url}">Google Account</a></b> 
                <i class="fab fa-google" style="color:#DB4437;"></i><br><br>""",
            unsafe_allow_html=True)
            else:
                # Check if token has expired:
                if token.is_expired():
                    if token.is_expired():
                        st.write(f"""<b>
                        Login session has ended,
                        please <a target="_self" href="{authorization_url}">
                        login</a> again.</b><br><br>""", unsafe_allow_html=True)
                else:
                    st.session_state["token"] = token
                    user_id, user_email = asyncio.run(
                        get_email(client=client,
                                  token=token['access_token'])
                    )
                    st.session_state["authentication_status"] = True
                    st.session_state["name"] = user_email
                    st.session_state["email"] = user_email

def login_google_oauth():
    CLIENT_ID = st.secrets["Google_OAuth_Client_ID"]
    CLIENT_SECRET = st.secrets["Google_OAuth_Client_Secret"]
    AUTHORIZE_ENDPOINT = st.secrets["Google_AUTHORIZE_ENDPOINT"]
    TOKEN_ENDPOINT = st.secrets["Google_TOKEN_ENDPOINT"]
    REVOKE_ENDPOINT = st.secrets["Google_REVOKE_ENDPOINT"]
    REDIRECT_URI = st.secrets["Google_OAuth_Redirect_URI"]

    if "authentication_status" not in st.session_state or st.session_state["authentication_status"] == None:
        # create a button to start the OAuth2 flow
        oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_ENDPOINT, TOKEN_ENDPOINT, TOKEN_ENDPOINT, REVOKE_ENDPOINT)
        result = oauth2.authorize_button(
            name="Continue with Google",
            icon="https://www.google.com.tw/favicon.ico",
            redirect_uri=REDIRECT_URI,
            scope="openid email profile",
            key="google",
            extras_params={"prompt": "consent", "access_type": "offline"},
            use_container_width=True,
        )

        if result:
            # decode the id_token jwt and get the user's email address
            id_token = result["token"]["id_token"]
            # verify the signature is an optional step for security
            payload = id_token.split(".")[1]
            # add padding to the payload if needed
            payload += "=" * (-len(payload) % 4)
            payload = json.loads(base64.b64decode(payload))
            email = payload["email"]
            st.session_state["token"] = result["token"]
            st.session_state["authentication_status"] = True
            st.session_state["name"] = email
            st.session_state["email"] = email
            st.rerun()

def login_github_oauth():
    CLIENT_ID = st.secrets["GitHub_OAuth_Client_ID"]
    CLIENT_SECRET = st.secrets["GitHub_OAuth_Client_Secret"]
    AUTHORIZE_ENDPOINT = st.secrets["GitHub_AUTHORIZE_ENDPOINT"]
    TOKEN_ENDPOINT = st.secrets["GitHub_TOKEN_ENDPOINT"]
    REDIRECT_URI = st.secrets["GitHub_OAuth_Redirect_URI"]

    if "authentication_status" not in st.session_state or st.session_state["authentication_status"] == None:
        oauth2 = OAuth2Component(CLIENT_ID, CLIENT_SECRET, AUTHORIZE_ENDPOINT, TOKEN_ENDPOINT, TOKEN_ENDPOINT, None)
        result = oauth2.authorize_button(
            name="Continue with GitHub",
            icon="https://github.com/favicon.ico",
            redirect_uri=REDIRECT_URI,
            scope="user:email",
            key="github",
            extras_params={},
            use_container_width=True,
        )

        if result:
            access_token = result["token"]["access_token"]
            headers = {"Authorization": f"token {access_token}"}
            user_data_response = requests.get("https://api.github.com/user/emails", headers=headers)

            if user_data_response.ok:
                emails = user_data_response.json()
                primary_email = next((email for email in emails if email['primary']), None)

                if primary_email:
                    email = primary_email["email"]
                    st.session_state["token"] = result["token"]
                    st.session_state["authentication_status"] = True
                    st.session_state["email"] = email
                else:
                    st.error("Primary email not found. Please check your GitHub email settings.")
                    st.write("Response:", emails)  # Debugging line
            else:
                st.error("Failed to retrieve user data.")
                st.write("Response Status Code:", user_data_response.status_code)  # Debugging line

            st.rerun()