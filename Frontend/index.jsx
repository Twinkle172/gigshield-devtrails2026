import React, { useState } from "react";

const AuthPage = () => {
  const [activeTab, setActiveTab] = useState("login");
  const [loginEmail, setLoginEmail] = useState("");
  const [signupEmail, setSignupEmail] = useState("");
  const [signupPassword, setSignupPassword] = useState("");
  const [message, setMessage] = useState("");
  const [messageColor, setMessageColor] = useState("#d9534f");

  const showForm = (type) => {
    setActiveTab(type);
    setMessage(""); // clear message when switching
  };

  const handleLogin = async () => {
    if (!loginEmail) {
      setMessage("Please enter your email.");
      setMessageColor("#d9534f");
      return;
    }

    try {
      const res = await fetch("http://127.0.0.1:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: loginEmail }),
      });

      const data = await res.json();
      setMessage(data.message);
      setMessageColor("#4CAF50");
    } catch (err) {
      setMessage("Login failed: " + err.message);
      setMessageColor("#d9534f");
    }
  };

  const handleSignUp = async () => {
    if (!signupEmail || !signupPassword) {
      setMessage("Please fill in all fields.");
      setMessageColor("#d9534f");
      return;
    }

    try {
      const res = await fetch("http://127.0.0.1:5000/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: signupEmail, password: signupPassword }),
      });

      const data = await res.json();
      setMessage(data.message);
      setMessageColor("#4CAF50");
    } catch (err) {
      setMessage("Sign Up failed: " + err.message);
      setMessageColor("#d9534f");
    }
  };

  return (
    <div style={styles.body}>
      <div style={styles.container}>
        <div style={styles.tabs}>
          <button
            style={{ ...styles.tabButton, ...(activeTab === "login" ? styles.activeTab : {}) }}
            onClick={() => showForm("login")}
          >
            Login
          </button>
          <button
            style={{ ...styles.tabButton, ...(activeTab === "signup" ? styles.activeTab : {}) }}
            onClick={() => showForm("signup")}
          >
            Sign Up
          </button>
        </div>

        {activeTab === "login" && (
          <div>
            <h2 style={styles.heading}>Login</h2>
            <label>Email:</label>
            <input
              type="email"
              placeholder="Enter your email"
              value={loginEmail}
              onChange={(e) => setLoginEmail(e.target.value)}
              style={styles.input}
            />
            <button onClick={handleLogin} style={styles.button}>
              Login
            </button>
          </div>
        )}

        {activeTab === "signup" && (
          <div>
            <h2 style={styles.heading}>Sign Up</h2>
            <label>Email:</label>
            <input
              type="email"
              placeholder="Enter your email"
              value={signupEmail}
              onChange={(e) => setSignupEmail(e.target.value)}
              style={styles.input}
            />
            <label>Password:</label>
            <input
              type="password"
              placeholder="Enter your password"
              value={signupPassword}
              onChange={(e) => setSignupPassword(e.target.value)}
              style={styles.input}
            />
            <button onClick={handleSignUp} style={styles.button}>
              Sign Up
            </button>
          </div>
        )}

        <div style={{ ...styles.message, color: messageColor }}>{message}</div>
      </div>
    </div>
  );
};

// Inline styles 
const styles = {
  body: {
    fontFamily: "Arial, sans-serif",
    background: "linear-gradient(135deg, #74ebd5, #ACB6E5)",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: "100vh",
    margin: 0,
  },
  container: {
    background: "#fff",
    padding: "30px",
    borderRadius: "10px",
    boxShadow: "0px 4px 15px rgba(0,0,0,0.2)",
    width: "320px",
  },
  heading: {
    marginBottom: "20px",
    color: "#333",
    textAlign: "center",
  },
  tabs: {
    display: "flex",
    justifyContent: "space-around",
    marginBottom: "20px",
  },
  tabButton: {
    width: "45%",
    background: "#eee",
    color: "#333",
    border: "none",
    padding: "10px",
    cursor: "pointer",
    borderRadius: "6px",
  },
  activeTab: {
    background: "#4CAF50",
    color: "white",
  },
  input: {
    width: "90%",
    padding: "10px",
    margin: "10px 0",
    border: "1px solid #ccc",
    borderRadius: "6px",
    fontSize: "14px",
  },
  button: {
    width: "100%",
    padding: "10px",
    background: "#4CAF50",
    color: "white",
    border: "none",
    borderRadius: "6px",
    fontSize: "16px",
    cursor: "pointer",
    transition: "background 0.3s ease",
  },
  message: {
    marginTop: "15px",
    fontSize: "14px",
    textAlign: "center",
  },
};

export default AuthPage;
