import init, { greet } from '/wasm/js/wasm_demo.js';
// https://rustwasm.github.io/docs/wasm-bindgen/examples/without-a-bundler.html

async function run() {
    await init();

    greet();
}

run();