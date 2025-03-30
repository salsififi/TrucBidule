import { defineConfig } from "vite";
import tailwindcss from "@tailwindcss/vite";

// Configuration entry point
export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
  base: "/static/",
  build: {
    manifest: "manifest.json",
    emptyOutDir: true,
    rollupOptions: {
      input: {
        app: "./src/main.js"
      }
    },
  },
});
