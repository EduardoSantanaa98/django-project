import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyA7z7cSzNkAeRiZOcGJOUu8vLMfDylVXUA",
  authDomain: "vue-replit.firebaseapp.com",
  projectId: "vue-replit",
  storageBucket: "vue-replit.firebasestorage.app",
  messagingSenderId: "625105729926",
  appId: "1:625105729926:web:c135a34a72dd941e9a9407",
  measurementId: "G-TRYKSNBFYC"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
