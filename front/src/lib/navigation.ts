export function navigateTo(url: string): void {
  if (typeof window !== "undefined") {
    window.location.href = url;
  }
}
