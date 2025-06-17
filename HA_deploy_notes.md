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


# to run with modifications
nextflow run -c nextflow/annotation.config nextflow/annotation.nf --cohort all_HA_vcf --input_dir nextflow/singleton_inputs
nextflow -c nextflow/talos.config run nextflow/talos.nf --matrix_table nextflow/test1_outputs/test1.mt/ --input_dir nextflow/singleton_inputs --cohort testpt2
