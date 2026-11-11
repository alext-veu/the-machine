# Pepper software and access recovery
Research snapshot: 11 November 2026.

## Platforms
- **NAOqi 2.5:** Linux robot services, Choregraphe, Python 2.7 and C++ SDKs, remote robot APIs.
- **NAOqi 2.9:** Android/QiSDK, Java/Kotlin applications. Not a drop-in replacement for 2.5 apps. Do not upgrade blindly.

## Recovery in order
1. Restore power, confirm hardware revision and installed NAOqi release. Do not use undocumented long-press startup or controller flash.
2. Observe tablet and speech; on suitable 2.5 builds, a single chest-button press announces the robot's IP address. Isolate on a test network.
3. Try documented default credentials **nao / nao** where applicable, via browser or SSH, or use known owner-provided credentials. Do not brute-force.
4. If authenticated, inventory and back up applications, configuration and firmware version before changing anything.
5. If the password was changed, consult documented vendor recovery. Factory reset of 2.5 may require linked Aldebaran account; manufacturer services might no longer function. Availability of a downloadable image does **not** imply the ability to flash a locked robot.
6. RobotLAB's offline image reinstall procedure requires existing SSH credentials; specialist recovery may be necessary. NAOqi 2.9 reset is different and can erase tablet apps/data.

## Sources
- [NAOqi 2.5 documentation](https://doc.aldebaran.com/2-5/)
- [Maxtronics 2.5 software/download archive](https://maxtronics.com/fr/support/kb/softwares/downloads-softwares/pepper-2-5-downloads/)
- [Maxtronics lost-password guidance](https://maxtronics.com/en/support/kb/pepper/troubleshooting/pepper-2-5-lost-or-forgotten-password/)
- [Maxtronics 2.5 factory reset](https://maxtronics.com/en/support/kb/pepper/advanced-operations/pepper-factory-reset-naoqi-2-5/)
- [Maxtronics 2.9 factory reset](https://maxtronics.com/fr/support/kb/pepper/advanced-operations/pepper-factory-reset-naoqi-2-9/)
- [RobotLAB system image reinstall](https://www.robotlab.com/support/factory-reset-on-pepper-robot/)
- [SoftBank 2.9 upgrade precautions](https://www.softbankrobotics.com.cn/index_files/pdf/NAOqi_2.9_Upgrade_en.pdf)
