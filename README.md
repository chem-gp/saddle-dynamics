# saddle-dynamics
GP-aided saddle-point molecular dynamics 


## Installation:

```
#!/usr/bin/env bash
# 

# Get conda:
# wget https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh

mkdir chem-gp && cd "$_"

# git clone git@github.com:chem-gp/fande.git
# git clone git@github.com:chem-gp/saddle-dynamics.git

git clone https://github.com/chem-gp/fande.git
git clone https://github.com/chem-gp/saddle-dynamics.git

# ...
if { conda env list | grep 'fande'; } >/dev/null 2>&1; 
then {
echo "conda fande environment found. Activating...";
conda activate fande;
}
else {
echo "Cannot find the environment. Creating new environment...";
conda env create -f fande/fande.yml;
conda activate fande;
}
# ...
fi;


# # Update environment from time to time:
# conda env update fande/fande.yml --prune


# Unzip archives:
# unzip dynamics.zip -d .
```


