{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-24.11";
  };

  outputs = { self, nixpkgs }: 

  let

    system = "x86_64-linux";
	pkgs = import nixpkgs {
	inherit system;
	};
	
	in
	{
		devShells.${system}.default = pkgs.mkShell {
			
		
			buildInputs = with pkgs; [
				python3
				pyright
			];
			shellHook = ''
			zsh
			'';
  };
};
}
