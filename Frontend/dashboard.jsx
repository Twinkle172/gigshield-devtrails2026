import React, { useState } from "react";

const Dashboard = () => {
  const [result, setResult] = useState("");

  const checkTrigger = async () => {
    try {
      const res = await fetch("http://127.0.0.1:5000/trigger-check");
      const data = await res.json();

      if (data.trigger) {
        setResult("✅ Payout: " + data.reason);
      } else {
        setResult("❌ No trigger");
      }
    } catch (err) {
      setResult("⚠️ Error: " + err.message);
    }
  };

  return (
    <div style={styles.container}>
      <h2>Dashboard</h2>
      <button onClick={checkTrigger} style={styles.button}>
        Check Trigger
      </button>
      <div style={styles.result}>{result}</div>
    </div>
  );
};

const styles = {
  container: {
    fontFamily: "Arial, sans-serif",
    margin: "30px",
  },
  button: {
    padding: "10px 20px",
    fontSize: "14px",
    cursor: "pointer",
    borderRadius: "6px",
    border: "none",
    backgroundColor: "#4CAF50",
    color: "white",
  },
  result: {
    marginTop: "20px",
    fontSize: "16px",
    fontWeight: "bold",
  },
};

export default Dashboard;
