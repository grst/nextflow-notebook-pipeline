#!/usr/bin/env nextflow

nextflow.enable.dsl = 2

include { JUPYTERNOTEBOOK as PARAMETRIZED_REPORT } from "./modules/nf-core/modules/jupyternotebook/main"


workflow {

    ch_iris = Channel.fromPath("data/iris.csv")

    PARAMETRIZED_REPORT(
        file("analyses/02_parametrized_report.py"),
        ch_iris.map{ it -> ["iris_path": it.name] },
        ch_iris
    )

}
