# Upstage의 Groundedness Check를 통한 RAG 성능 평가

## 기능
- 최신 LLM인 llama3.2를 사용할 수 있음
- Upstage의 Groundedness Check를 통해 RAG 성능을 평가
- 임베딩 포함 전과정을 완전 무료화

## 필요한 것
- Python 3.10
- Ollama 0.3.12
- Upstage API 키

## 사용 방법
1. Ollama를 설치합니다
   ```
   https://ollama.com/download
   ```
2. 필요한 라이브러리를 설치합니다
   ```
   pip install -r requirements.txt
   ```
3. .env파일에서 Upstage API 키와 PDF file path를 환경 변수로 설정합니다
