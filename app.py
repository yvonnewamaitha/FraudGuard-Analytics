# GEMINI_API_KEY: Required for Gemini AI API calls.
# AI Studio automatically injects this at runtime from user secrets.
# Users configure this via the Secrets panel in the AI Studio UI.
GEMINI_API_KEY="MY_GEMINI_API_KEY"

# APP_URL: The URL where this applet is hosted.
# AI Studio automatically injects this at runtime with the Cloud Run service URL.
# Used for self-referential links, OAuth callbacks, and API endpoints.
APP_URL="MY_APP_URL"
node_modules/
build/
dist/
coverage/
.DS_Store
*.log
.env*
!.env.example
"""
FraudGuard Analytics - Prototype Python Script
Designed for Google Colab

This script demonstrates a Decision Tree model for fraud detection.
It includes synthetic data generation, model training, and a simple CLI interface.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree, export_text
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# 1. Generate Synthetic Dataset
def generate_data(n=1000):
    np.random.seed(42)
    
    # Features
    transaction_amount = np.random.uniform(10, 10000, n)
    transaction_time = np.random.randint(0, 24, n)
    location_change = np.random.choice([0, 1], n, p=[0.8, 0.2])
    previous_fraud_history = np.random.choice([0, 1], n, p=[0.9, 0.1])
    
    # Logic for fraud label (Simulating a real-world scenario)
    # Fraud is more likely if:
    # - Amount is very high (> 5000)
    # - Location changed AND amount is high
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>My Google AI Studio App</title>
  </head>
  <body>
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>
{
  "name": "FraudGuard Analytics",
  "description": "A professional fintech dashboard for real-time payment fraud detection using interpretable machine learning models.",
  "requestFramePermissions": []
}
{
  "name": "react-example",
  "version": "0.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "react-example",
      "version": "0.0.0",
      "dependencies": {
        "@google/genai": "^1.29.0",
        "@tailwindcss/vite": "^4.1.14",
        "@vitejs/plugin-react": "^5.0.4",
        "clsx": "^2.1.1",
        "dotenv": "^17.2.3",
        "express": "^4.21.2",
        "lucide-react": "^0.546.0",
        "motion": "^12.23.24",
        "react": "^19.0.0",
        "react-dom": "^19.0.0",
        "recharts": "^3.8.1",
        "tailwind-merge": "^3.5.0",
        "vite": "^6.2.0"
      },
      "devDependencies": {
        "@types/express": "^4.17.21",
        "@types/node": "^22.14.0",
        "autoprefixer": "^10.4.21",
        "tailwindcss": "^4.1.14",
        "tsx": "^4.21.0",
        "typescript": "~5.8.2",
{
  "name": "react-example",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite --port=3000 --host=0.0.0.0",
    "build": "vite build",
    "preview": "vite preview",
    "clean": "rm -rf dist",
    "lint": "tsc --noEmit"
  },
  "dependencies": {
    "@google/genai": "^1.29.0",
    "@tailwindcss/vite": "^4.1.14",
    "@vitejs/plugin-react": "^5.0.4",
    "clsx": "^2.1.1",
    "dotenv": "^17.2.3",
    "express": "^4.21.2",
    "lucide-react": "^0.546.0",
    "motion": "^12.23.24",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "recharts": "^3.8.1",
    "tailwind-merge": "^3.5.0",
    "vite": "^6.2.0"
  },
  "devDependencies": {
    "@types/express": "^4.17.21",
    "@types/node": "^22.14.0",
import React, { useState } from 'react';
import { 
  LayoutDashboard, 
  ShieldAlert, 
  BarChart3, 
  Settings, 
  Search, 
  Bell, 
  User,
  ArrowUpRight,
  ArrowDownRight,
  AlertTriangle,
  CheckCircle2,
  ChevronRight,
  Info,
  CreditCard,
  Clock,
  MapPin,
  History,
  Download
} from 'lucide-react';
import { 
  AreaChart, 
  Area, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer,
  PieChart,
@import "tailwindcss";
import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}
import {StrictMode} from 'react';
import {createRoot} from 'react-dom/client';
import App from './App.tsx';
import './index.css';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
import { Type } from "@google/genai";

export interface Transaction {
  amount: number;
  time: number; // 0-23
  locationChange: boolean;
  previousHistory: boolean;
}

export interface PredictionResult {
  isFraud: boolean;
  riskScore: number;
  decisionPath: string[];
}

/**
 * A simple interpretable decision tree implementation for the prototype.
 */
export function predictFraud(tx: Transaction): PredictionResult {
  const path: string[] = [];
  let riskScore = 0;
  let isFraud = false;

  path.push("Start Analysis");

  // Rule 1: Previous Fraud History
  if (tx.previousHistory) {
    path.push("Previous fraud history detected (+40% risk)");
    riskScore += 40;
  } else {
    path.push("No previous fraud history (0% risk)");
£5,000 (+50% risk)");
    riskScore += 50;
  } else if (tx.amount > 1000) {
    path.push("Transaction amount > £1,000 (+20% risk)");
    riskScore += 20;
  } else {
    path.push("Transaction amount is within normal range (0% risk)");
  }

  // Rule 3: Location Change
  if (tx.locationChange) {
    path.push("Sudden location change detected (+30% risk)");
    riskScore += 30;
  }

  // Rule 4: Time of Transaction (Night time risk)
  if (tx.time >= 0 && tx.time <= 5) {
    path.push("Transaction occurred during high-risk hours (00:00 - 05:00) (+15% risk)");
    riskScore += 15;
  }

  // Final Decision
  riskScore = Math.min(riskScore, 100);
{
  "compilerOptions": {
    "target": "ES2022",
    "experimentalDecorators": true,
    "useDefineForClassFields": false,
    "module": "ESNext",
    "lib": [
      "ES2022",
      "DOM",
      "DOM.Iterable"
    ],
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "isolatedModules": true,
    "moduleDetection": "force",
    "allowJs": true,
    "jsx": "react-jsx",
    "paths": {
      "@/*": [
        "./*"
      ]
    },
    "allowImportingTsExtensions": true,
    "noEmit": true
  }
}
import tailwindcss from '@tailwindcss/vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import {defineConfig, loadEnv} from 'vite';

export default defineConfig(({mode}) => {
  const env = loadEnv(mode, '.', '');
  return {
    plugins: [react(), tailwindcss()],
    define: {
      'process.env.GEMINI_API_KEY': JSON.stringify(env.GEMINI_API_KEY),
    },
    resolve: {
      alias: {
        '@': path.resolve(__dirname, '.'),
      },
    },
    server: {
      // HMR is disabled in AI Studio via DISABLE_HMR env var.
      // Do not modifyâfile watching is disabled to prevent flickering during agent edits.
      hmr: process.env.DISABLE_HMR !== 'true',
    },
  };
});
