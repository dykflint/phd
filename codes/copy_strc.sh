#!/bin/bash
for f in *.strc
do
        [[ -f "$f" ]] || continue # skip if not regular file
        dir="${f%.*}"
        cp "$f" "../run/$dir"
done
