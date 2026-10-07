# The Machine · Primary Assets

Original, unofficial Person of Interest fan experience for Alexander, Victor, Boris and Toffee. Procedural visuals and Web Audio synthesis; no television assets. All subjects, feeds and case numbers are fictional.

## Development

`npm install`, then `npm run dev`. `npm run build` runs strict TypeScript and creates the static production bundle in `dist/`.

React 19, TypeScript, Vite, Three.js, React Three Fiber, Drei and Zustand. Story definitions live in `src/data.ts`; persisted transitions and command dispatch live in `src/store.ts`. 3D rendering is lazy loaded. Buildings are instanced, outlines and architecture edges are batched, and mobile uses a smaller city. A 2D fallback preserves the modules if WebGL is unavailable. Progress is saved to this browser only.

## Controls

Drag to orbit, right drag to pan, wheel/pinch to zoom. Select labels to track subjects or acquire cameras. Module navigation works with Tab and Enter. Backtick opens the terminal, P toggles POV and Escape closes the module. Audio starts only through the sound control. Reduced motion stops city motion and animated feeds.

## QA

`qa/browser.js` is a browser interaction journey for the Playwright CLI (`run-code --filename=qa/browser.js`). It exercises the character commands, unlock gates, five feline sightings, complete story, secret ending, persistence, mute, four feeds, simulations, reset, mobile terminal and reduced motion. Run against a local preview; the journey resets its own local progress. `qa/final.js` checks the final desktop/mobile views, keyboard flow and deliberately unavailable WebGL.

Production publishing uses the Sites source workflow helper and the private deployment operation. `.openai/hosting.json` retains the Site identity.
