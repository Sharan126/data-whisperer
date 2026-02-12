# DataWhisperer 🧠📊

**The AI That Talks to Your Spreadsheets**

DataWhisperer is a serverless application that allows users to upload CSV files and ask questions in plain English. It uses **AWS Lambda** for compute and **Amazon Bedrock (Claude 3 Haiku)** for natural language understanding and code generation.

## 🚀 Feature
- **Project Type**: Serverless Web App
- **Key Services**: Amazon S3, AWS Lambda, Amazon Bedrock
- **AI Model**: Anthropic Claude 3 Haiku

## 🛠️ Architecture
- **Frontend**: React (S3 static hosting / Vercel)
- **Backend**: AWS Lambda (Python)
- **Storage**: Amazon S3
- **AI**: Amazon Bedrock

## 📦 Setup & Deployment

### Prerequisites
- AWS Account with Bedrock Model Access enabled (Claude 3 Haiku)
- AWS CLI installed and configured
- Python 3.9+

### Backend (Lambda)
1. Navigate to the `backend` code.
2. Zip the `lambda_function.py`.
3. Create a Lambda function in AWS Console.
4. Upload the zip code.
5. Attach an IAM role with `bedrock:InvokeModel` permissions.

### Usage
This is a demo project for the **AWS Builder Center**.
See the [full blog post](TODO: Insert Blog Link) for details.
