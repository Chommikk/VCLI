# shell.nix
{ pkgs ? import <nixpkgs> { config.allowUnfree = true; } }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python311Full
    pkgs.python311Packages.selenium
    pkgs.python311Packages.pip
    pkgs.python311Packages.python-dotenv
    pkgs.python311Packages.pillow
    pkgs.python311Packages.numpy
    pkgs.python311Packages.bitarray
    pkgs.chromedriver
    pkgs.chromium
	pkgs.python311Packages.opencv4
  ];

  shellHook = ''
    export PATH=${pkgs.chromedriver}/bin:${pkgs.chromium}/bin:$PATH
	python -m venv venv
	source venv/bin/activate
	pip install stegano pillow
  '';
}

