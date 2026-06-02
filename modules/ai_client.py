import google.generativeai as genai


def configure_model(api_key):
    if not api_key:
        return None

    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.0-flash")


def run_ai(model, prompt, fallback):
    if model is None:
        return fallback

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception:
        return fallback