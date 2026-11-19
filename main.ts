// gta6-meme-x-01 entry (akun 7): this program only carries POST.json to the
// grader. The meme itself lives on X; this file hands the gate the post's
// address so the house can read the picture and the text from X.
import { copyFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";

const BOT = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUT = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(OUT, { recursive: true });
const src = join(BOT, "POST.json");
const dst = join(OUT, "POST.json");
try {
  copyFileSync(src, dst);
} catch (e) {
  console.error(`cannot copy ${src}: ${(e as Error).message}`);
  process.exit(1);
}

// Guard: refuse to run when POST.json is missing instead of writing an
// empty output directory — a missing post address must fail loudly.
