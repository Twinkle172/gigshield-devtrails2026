import React, { useEffect, useState } from "react";

const Wallet = () => {
  const [balance, setBalance] = useState(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchBalance = async () => {
      try {
        const res = await fetch("http://127.0.0.1:5000/wallet");
        const data = await res.json();
        setBalance(data.balance);
      } catch (err) {
        setError("⚠️ Error fetching balance: " + err.message);
      }
    };

    fetchBalance();
  }, []); // runs once when component mounts

  return (
    <div style={styles.container}>
      <h2>Wallet</h2>
      {error ? (
        <div style={styles.error}>{error}</div>
      ) : balance !== null ? (
        <div style={styles.balance}>Balance: ₹{balance}</div>
      ) : (
        <div style={styles.loading}>Loading...</div>
      )}
    </div>
  );
};

const styles = {
  container: {
    fontFamily: "Arial, sans-serif",
    margin: "30px",
  },
  balance: {
    fontSize: "18px",
    fontWeight: "bold",
    color: "#4CAF50",
  },
  error: {
    fontSize: "16px",
    color: "#d9534f",
  },
  loading: {
    fontSize: "16px",
    color: "#555",
  },
};

export default Wallet;
