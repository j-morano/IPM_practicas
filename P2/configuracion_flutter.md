# Instalación y configuración de Flutter

## Flutter/Dart

Para instalar Flutter, es necesario seguir los pasos que se indican en <https://docs.flutter.dev/get-started/install>.

Dart SDK viene incluído con Flutter, por lo que no es necesario instalarlo aparte. De todos modos, si se quiere, se puede instalar siguiendo estas instrucciones: <https://dart.dev/get-dart>


## Android SDK

### Línea de comandos

Además, para la emulación del dispositivo móvil, también es conveniente instalar Android SDK: <https://developer.android.com/studio/index.html>.

Para que funcione, es necesario crear una carpeta bajo la raíz `cmdline-tools`, e.g. `latest` y mover el contenido de la carpeta `cmdline-tools` a la recién creada.

```shell
# Listar los paquetes disponibles
./sdkmanager --list

# Instalar los paquetes necesarios
./sdkmanager "system-images;android-28;default;x86"
./sdkmanager "platforms;android-28"
./sdkmanager "build-tools;28.0.3"

# Crear dispositivo AVD
./avdmanager create avd --name android28 --package "system-images;android-28;default;x86"

# Establecer el path del Android SDK en flutter
flutter config --android-sdk ANDROID_SDK_PATH

# Ejecutar emulador con el dispositivo creado
./emulator @android28
```
