import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
// import "../ML Integrate/app.py";
import { AppProvider } from './context'
import { Auth0Provider } from "@auth0/auth0-react";

ReactDOM.createRoot(document.getElementById('root')).render(
  <Auth0Provider
  domain="dev-pifl00kkz2wqirim.us.auth0.com"
  clientId="UiOnrVAolo7nVNMtW0nusaGZPWz2DdSd"
  authorizationParams={{
    redirect_uri: window.location.origin
  }}>
  <AppProvider>
    <App />
  </AppProvider>
  </Auth0Provider>
);

// export 