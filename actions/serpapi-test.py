from serpapi import GoogleSearch
import pprint

params = {
  "q": "How do I get fit?",
  "hl": "en",
  "gl": "us",
  "google_domain": "google.com",
  "api_key": "109578248b35fe6863d9c0bf9ceed8938f411aeada9fb737e49a422674e2f805"
}


if __name__ == "__main__":
    search = GoogleSearch(params)
    results = search.get_dict()
    print(f'Here an idea: {"".join(results["answer_box"]["list"])}')
    print(f'Please see the following link for more inforamtion: {results["answer_box"]["link"]}')