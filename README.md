# Upstage의 Groundedness Check를 통한 RAG 성능 평가

## 기능
- 최신 LLM인 llama3.2를 사용할 수 있음
- Upstage의 Groundedness Check를 통해 RAG 성능을 평가
- 임베딩 포함 전과정 무료화

## 필요한 것
- Python 3.10
- Ollama 0.3.12
- Upstage API 키

## 사용 방법
1. 다음 경로에서 Ollama를 설치합니다.
   ```
   https://ollama.com/download
   ```
2. 필요한 라이브러리를 설치합니다.
   ```
   pip install -r requirements.txt
   ```
3. .env파일에서 Upstage API 키와 PDF file path를 환경 변수로 설정합니다.
   
4. powershell에서 다음 스크립트를 실행합니다.
   ```
   ollama run llama3.2
   ```
5. q_list에 RAG 평가 질문들을 입력합니다.
   
6. 다음 스크립트를 실행합니다.
   ```
   python main.py
   ```

## 예시
- 한국은행「금융안정보고서」(2024년 6월)를 사용하여 만든 예시
   ```
   https://eiec.kdi.re.kr/policy/materialView.do?num=253308
   ```
- 사용한 질문은 2개 "What is the outlook for the Korean economy when assessing the risks?", "What are the factors that could pose a threat to the economy?"
- 평가 결과
  ![example](https://github.com/user-attachments/assets/2be3c59a-b1b4-4167-8620-4ca0d736ede8)
