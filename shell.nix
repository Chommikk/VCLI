# shell.nix
{ pkgs ? import <nixpkgs> {config.allowUnfree = true;} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python311Full
    pkgs.python311Packages.selenium
    pkgs.python311Packages.python-dotenv
	pkgs.chromedriver
	pkgs.chromium
  ];
 
	shellHook = ''
		export PATH=${pkgs.chromedriver}/bin:${pkgs.chromium}/bin:$PATH
	'';
}

