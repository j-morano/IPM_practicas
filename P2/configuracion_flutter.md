# Instalación y configuración de Flutter

## Flutter/Dart

Para instalar Flutter, es necesario seguir los pasos que se indican en <https://docs.flutter.dev/get-started/install>.

Después, es necesario añadir el binario de flutter al `$PATH`:
```shell
ln -s /snap/bin/flutter ~/.local/bin/flutter
```

Dart SDK viene incluído con Flutter, por lo que no es necesario instalarlo aparte. De todos modos, si se quiere, se puede instalar siguiendo estas instrucciones: <https://dart.dev/get-dart>


## Android SDK

Para la emulación del dispositivo móvil, es conveniente instalar Android SDK: <https://developer.android.com/studio/index.html>.

Esto se puede hacer por medio de la instalación de Android Studio, pero también es común hacerlo mediante el cliente de línea de comandos.

### Línea de comandos

#### Prerrequisitos


Para que el Android SDK funcione, antes es necesario instalar el Java Development Kit.
Por ejemplo, en distribuciones basadas en Debian, este puede instalarse por medio de los siguientes comandos:

```shell
sudo apt install openjdk-17-jre openjdk-17-jdk
```

Además, es necesario crear una carpeta bajo la raíz `cmdline-tools`, e.g. `latest` y mover el contenido de la carpeta `cmdline-tools` a la recién creada.

```shell
mkdir .latest/
mv * .latest/
mv .latest/ latest/
```

#### Creación de un dispositivo virtual Android

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
