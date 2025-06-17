# On mac - build from dockerfile and push to dockerhub
docker build -t talos:7.1.5 .
docker tag talos:7.1.5 jameslawlor/talos-build:7.1.5
docker push jameslawlor/talos-build:7.1.5


# convert to SIF file
singularity pull docker://jameslawlor/talos-build:7.1.5
# push singularity image to SyLabs
singularity key newpair
singularity sign talos-build_7.1.5.sif
singularity remote add james_lawlor library://james_lawlor/
singularity push talos-build_7.1.5.sif library://james_lawlor/talos-build/talos-build:7.1.5
