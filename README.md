
# Question-Answering Bot API

This API generates answers based on questions asked and documents uploaded.

## API Endpoint

### `/qna`

The `/qna` API accepts two files:
- A questions file in JSON format.
- A document file, which can be either JSON or PDF format.

### Sample API Request

You can test the API using the following `curl` command:

```bash
curl --location 'http://0.0.0.0:8000/qna' \
--form 'questions_file=@"<file_path>.json"' \
--form 'document_file=@"<file_path>.json"'
```
## Installation 
### Local Development 
1. Clone this repository. 
2.  Create a `.env` file based on the sample provided (`.sample.env`). 
3. Set the `OPENAI_API_KEY` environment variable in your `.env` file with your valid OpenAI API key. 
### Docker 
1. Build the Docker image using the provided commands or tools specific to your environment.
2. Run the container using the included `docker_run_helper.py` script: ```bash python3 docker_run_helper.py <image_id> <container_name> <env_file_name>```
