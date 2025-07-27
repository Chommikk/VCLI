# shell.nix
{ pkgs ? import <nixpkgs> {config.allowUnfree = true;} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python311Full
    pkgs.python311Packages.selenium
	pkgs.chromedriver
	pkgs.chromium
  ];
 
	shellHook = ''
		export PATH=${pkgs.chromedriver}/bin:${pkgs.chromium}/bin:$PATH
	'';
}

