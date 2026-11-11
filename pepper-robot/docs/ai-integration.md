# External AI integration design

## Recommended topology

```text
Person -> Pepper microphone/cameras/tablet
                  |  isolated LAN, NAOqi or QiSDK
                  v
          External AI bridge (Python / mini PC)
          - streaming speech-to-text
          - language model (cloud API or Ollama)
          - session/context and optional knowledge base
          - text-to-speech / gestures
          - safety allowlist and audit
                  |
                  v
          Pepper speakers, head, arms, tablet
```

The original Atom processor controls robotics; an optional Raspberry Pi 5 or modern x86 mini PC handles modern software and storage. Start with a laptop. Do not assume Pepper RAM/eMMC can be upgraded, or draw power from undocumented USB/service lines.

## Milestones
1. Identify running NAOqi version and reach documented robot API over isolated LAN.
2. Text-to-speech: Pepper says 'I'm back'.
3. Head tracking and safe short gesture with human supervision.
4. Push-to-talk: speech transcription -> LLM -> Pepper TTS.
5. Optional vision, FAQ retrieval, tablet UI and opt-in memory.
6. Evaluate internal mounting, power supply and cooling only after external proof of concept.

## Guardrails
Keep emergency stop operational; never send raw model output directly to actuators. Constrain actions by speed, posture and ranges; no unsupervised locomotion in early testing. Isolate old robotics software from enterprise networks. Keep API keys outside Git and obtain consent before recording voices/images.

## Potential uses
AI reception guide, campus robotics demonstrations, IT status announcer (read-only), STEM programming projects, exhibit narrator and conversational companion.
