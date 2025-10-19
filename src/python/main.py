from datetime import datetime
import time

def generate_caption(topic: str) -> str:
    # Placeholder safe example — no platform automation.
    ts = datetime.utcnow().isoformat()
    return f"[{ts}] Tips about {topic}: Focus on value, avoid spam, be authentic."

if __name__ == '__main__':
    topics = ['growth', 'ai', 'marketing']
    for t in topics:
        print(generate_caption(t))
        time.sleep(1)
