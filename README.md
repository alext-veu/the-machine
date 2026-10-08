# The Machine · Primary Assets

Original, unofficial Person of Interest fan experience for Alexander, Victor, Boris and Toffee. Procedural visuals and Web Audio synthesis; no television assets. All subjects, feeds and case numbers are fictional.

**Play:** [The Machine — Primary Assets](https://the-machine-primary-assets.alext24979.chatgpt.site/)

**Source:** [alext-veu/the-machine](https://github.com/alext-veu/the-machine) — private repository.

## Playing the experience

1. Let initialisation finish, or select **Skip initialisation**.
2. Select city markers or open **Assets** to track a subject.
3. Switch between **City Map**, **Machine POV** and **Network**.
4. Acquire simulated feeds through **Cameras**.
5. Open the incoming **Number** to read a case and evaluate an intervention.
6. Open **Events** and inspect the first packet to begin the investigation.
7. Open **Terminal** and enter `HELP` for commands and archive keys.

Enable audio with the speaker control. Sound starts only after your interaction; volume controls are in **System**. Panels scroll internally, and their minus button minimises them.

### Terminal reference

Commands ignore letter case. Submit with Enter or the arrow button.

| Command | Result |
| --- | --- |
| `HELP` | List commands and archive keys |
| `STATUS` | Report system and story state |
| `ASSETS`, `CAMERAS`, `NUMBERS` | Open subjects, feeds or fictional cases |
| `EVENTS`, `NETWORK`, `ARCHIVE` | Open investigation, relationships or discoveries |
| `SIMULATE` | Open the branching simulation engine |
| `INVESTIGATE` | Advance one investigation step |
| `FIND TOFFEE` | Search for the feline asset |
| `MAP`, `POV` | Change the city view and close the panel |
| `CLEAR`, `EXIT` | Clear terminal output or close the panel |

## Clues — reveal only what you need

You do not need to wait for random events. Investigation progresses through the actions in **Events**. These clues leave the mystery's reveal and final ending undisclosed.

- **Alexander:** the Machine recognises its administrator. The terminal may accept a role as readily as a name.
- **Violeta:** follow evidence through Events: a packet, an interrupted feed and correlated routes. Observe before judging.
- **Toffee:** a cat leaves traces in several systems. Look in the city, files, camera imagery and relationship graph.
- **Archives:** familiar names from the series can act as search keys. A bird-like filename points toward a familiar creator.
- **Two animals:** search for the loyal canine, then quickly look for the less cooperative feline.
- **The ending:** Archive tracks discoveries. Its reconstruction control explains what is still missing.

<details>
<summary>Stronger clue: administrator and internal architecture</summary>

Enter `ADMIN` to unlock Alexander's controls. Then use the Admin panel or enter `GOD MODE` to reveal the internal 3D graph. Enter the mode command again to turn it off; its discovery remains recorded.

</details>

<details>
<summary>Stronger clue: analog interface and external intelligence</summary>

Try `ROOT` and `SAMARITAN` in the terminal. Each briefly changes the atmosphere and records a discovery. Other character archive keys appear in `HELP`.

</details>

<details>
<summary>Stronger clue: feline discoveries and protocol</summary>

Five **different** evidence sources unlock Toffee Protocol. Repeating a source does not increase the count. Six sources are available:

- Select Toffee's city marker.
- Select Toffee in Assets.
- Search for Toffee in the terminal.
- Inspect the feline silhouette in a camera feed.
- Inspect the hidden feline node in Network.
- Inspect the feline interference record in Archive.

Archive shows your sighting count. `TOFFEE MODE` toggles a separate feline-obsessed mode; it does not replace completing the sighting chain.

For the cross-species analysis, search `BEAR`, then search for Toffee within 30 seconds.

</details>

<details>
<summary>Stronger clue: family messages</summary>

Try `FAMILY` for a status report and `PIZZA` for a proposed dispute resolution. The Machine's confidence is not always justified.

</details>

<details>
<summary>Final archive checklist — unlock requirements, without the ending</summary>

Discover all six records:

1. ADMIN access.
2. GOD MODE.
3. Root's analog-interface event.
4. Samaritan's external-signature event.
5. Toffee Protocol, through five distinct feline sighting sources.
6. Violeta's completed investigation, including resolution in Events.

Then select **Reconstruct final archive** in Archive or enter `FINAL`. If incomplete, the Machine returns a hint. Modes do not need to remain active after their discoveries are recorded.

</details>

## Progress and reset

Story progress, discoveries, feline sightings, initialisation status and administrator / GOD MODE unlocks are saved in this browser. Master volume is saved separately. Terminal history, transient notices and Toffee Mode are session state.

Progress does not automatically transfer between devices, browsers, private sessions or localhost and the live Site.

To start again, unlock **Admin**, select **Reset experience**, then confirm. Cancel keeps your discoveries. Reset clears adventure progress but retains the separately saved master-volume setting.

## Development

Use Node.js **22.12 or newer** and npm. Clone the private repository with an authorised GitHub account, then install from the lockfile:

```sh
git clone https://github.com/alext-veu/the-machine.git
cd the-machine
npm ci
npm run dev
```

Open the local URL printed by Vite. No backend credentials are required to play locally.

For a production build and preview:

```sh
npm run check
npm run build
npx vite preview --host 127.0.0.1
```

`npm run build` runs strict TypeScript and creates the static bundle in `dist/`. Preview normally serves at `http://127.0.0.1:4173/`; use the printed port if it is occupied.

React 19, TypeScript, Vite, Three.js, React Three Fiber, Drei and Zustand. Story definitions live in `src/data.ts`; persisted transitions and command dispatch live in `src/store.ts`. 3D rendering is lazy loaded. Buildings are instanced, outlines and architecture edges are batched, and mobile uses a smaller city. A 2D fallback preserves the modules if WebGL is unavailable. Progress is saved to this browser only.

## Controls

Drag to orbit, right drag to pan, wheel/pinch to zoom. Select labels to track subjects or acquire cameras. Module navigation works with Tab and Enter. Backtick opens the terminal, P toggles POV and Escape closes the module. Audio starts only through the sound control. Reduced motion stops city motion and animated feeds.

On phones, use one-finger drag to orbit, pinch to zoom and two-finger drag to pan. All eight modules are in the bottom dock. Use the district selector or focused-asset button to change targets. In the terminal, Up / Down recalls commands when using an external keyboard.

## QA

`qa/browser.js` is a browser interaction journey for the Playwright CLI (`run-code --filename=qa/browser.js`). It exercises the character commands, unlock gates, five feline sightings, complete story, secret ending, persistence, mute, four feeds, simulations, reset, mobile terminal and reduced motion. Run against a local preview; the journey resets its own local progress. `qa/final.js` checks the final desktop/mobile views, keyboard flow and deliberately unavailable WebGL.

Start the production preview on port 4173, then run the browser journeys with the Playwright CLI:

```sh
npx --yes --package @playwright/cli playwright-cli open http://127.0.0.1:4173/
npx --yes --package @playwright/cli playwright-cli run-code --filename=qa/browser.js
npx --yes --package @playwright/cli playwright-cli run-code --filename=qa/final.js
npx --yes --package @playwright/cli playwright-cli run-code --filename=qa/phone.js
```

**The full browser journey clears the preview browser's existing adventure progress.** Screenshots are saved in `output/playwright/`, which is ignored by Git.

## Phone layout

`src/phone.css` provides a touch dock with all eight modules, sheet panels, larger controls and Safari safe-area padding. `usePhoneViewport` follows the visual viewport when the software keyboard opens; terminal inputs use 16px text. Coarse-pointer devices use a bounded 1x 3D pixel ratio, and short landscape viewports also use the smaller city. Progress is shared with the desktop layout in the same browser.

`qa/phone.js` checks touch-enabled emulated phone viewports at 393×852, 430×932, 402×874, 440×956 and 852×393, including dock bounds, terminal commands, camera switching, district and case navigation, and a simulated keyboard viewport. Physical iPhone Safari testing has not been performed. The Site is public; use the general saved-version deployment operation for updates.

## Source sync and publishing

The local `main` branch tracks `origin/main` in this private GitHub repository. Sync reviewed changes with:

```sh
git pull --ff-only
git add <changed-files>
git commit -m "Describe the change"
git push
```

GitHub stores the source and commit history; pushing does **not** automatically publish to ChatGPT Sites. Site updates use the Sites source workflow to package the exact source state, save a version and deploy it. Retain the Site identity in `.openai/hosting.json` and its public audience. GitHub repository privacy is independent of the live Site's visibility.

## Manhattan map

The map uses NYC Open Data building footprints and roof heights (5zhs-2jue), named street centerlines (inkn-q76z), and shoreline-clipped borough boundaries (gthc-hcne). All 45,194 Manhattan building footprints are bundled. Buildings are simplified flat roof extrusions, with a 4 m fallback where a roof height is absent. Street and avenue names appear at closer zoom levels, with collision spacing for phones. The surveillance identities, camera feeds and traffic remain fictional. Central Park is a schematic green overlay.

Select a district to focus its area, then scroll/pinch to zoom and drag to orbit. North is negative Z; scene units represent 100 metres. Geometry uses a local WGS84 approximation centered at 73.975° W, 40.78° N, quantized to 1 m. The initial map download includes approximately 11 MB of compressed building geometry and is cached within the session. No map API key is required.

Regenerate the bundled snapshot with `node scripts/build-manhattan.mjs` (requires network access), then `npm run build`. Data sources: [Buildings](https://data.cityofnewyork.us/City-Government/BUILDING/5zhs-2jue), [Streets](https://data.cityofnewyork.us/City-Government/Centerline/inkn-q76z), [Boundary](https://data.cityofnewyork.us/City-Government/Borough-Boundaries/gthc-hcne).

## Map navigation

Default **Pan**: drag with the left mouse button or one finger to move over the map. Switch to **Rotate** for orbiting and tilting. Right mouse drag performs the alternate action. Use the mouse wheel/trackpad scroll or pinch with two fingers to zoom. In Pan mode two fingers also rotate; in Rotate mode two fingers also pan. The toolbar provides zoom, rotate, directional pan, face north and reset view buttons. Automatic GOD MODE camera rotation is disabled to keep navigation under your control. Focus the map with Tab for arrow key panning, +/− zoom, R rotation and 0 reset. Open GESTURES for contextual guidance.

## Landmarks, lighting and brass clocks

DAY / NIGHT changes map lighting and colors without moving the camera. EXPLORE LANDMARKS focuses six original, stylized models: Empire State Building, Chrysler Building, One World Trade Center, Flatiron Building, Brooklyn Bridge and Statue of Liberty. Crowns, spires, windows, bridge towers/cables and the copper-green statue are schematic details, not survey-grade replicas. Central Park includes a stylized tree canopy and reservoir. The four original building extrusions are replaced using official NYC footprint matches saved in `public/map/landmark-footprints.json`. Regeneration preserves these replacements.

WORLD CLOCKS opens four polished brass analog dials with digital time and date: device-local, New York, London and Tokyo. Time comes from the device clock; IANA time zones in Intl handle daylight saving automatically. Clocks render as scalable original SVG with metallic bezels, engraved Roman numerals, glass highlights and live hands. No external clock service is required.
