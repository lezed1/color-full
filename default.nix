with import <nixpkgs> {};

let
  openrazer = (import /home/zander/gits/nixpkgs-openrazer {}).python3Packages.openrazer;
in

stdenv.mkDerivation rec {
  name = "colorfull";
  # env = buildEnv { name = name; paths = buildInputs; };
  buildInputs = [
    python3
    mypy
    openrazer
  ] ++ (with python3Packages; [
    # openrazer
    attrs
    numpy
  ]);
}
