export function schedulePost(task: () => void, delayMs: number) {
  setTimeout(task, delayMs);
}

export function runDemo() {
  schedulePost(() => {
    console.log('Posting demo content (safe, no API calls).');
  }, 1000);
}

if (require.main === module) {
  runDemo();
}
