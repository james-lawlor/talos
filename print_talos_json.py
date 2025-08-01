import json
import csv
import sys

with open(sys.argv[1], 'r') as f:
    data = json.load(f)
 
columns = ['sample', 'chrom', 'pos', 'ref', 'alt', 'categories', 'gene', 'consequence', 'dna_change',
            'clinvar_significance', 'date_of_phenotype_match',
            'evidence_last_updated', 'first_tagged']

with open(sys.argv[2], 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=columns, delimiter='\t')
    writer.writeheader()

    for sample_id, sample_data in data.get("results", {}).items():
        for variant in sample_data.get("variants", []):
            #mane_csq = variant.get('transcript_consequences', [])
            #mane_csq = [x for x in mane_csq if x['mane'] == '1']
            first_trans = variant.get('var_data', {}).get('transcript_consequences', [])
            try:
                first_trans = first_trans[0]
            except IndexError:
                first_trans = {}
            row = {
                'sample': variant.get('sample', ''),
                'chrom': variant.get('var_data', {}).get('coordinates', {}).get('chrom', ''),
                'pos': variant.get('var_data', {}).get('coordinates', {}).get('pos', ''),
                'ref': variant.get('var_data', {}).get('coordinates', {}).get('ref', ''),
                'alt': variant.get('var_data', {}).get('coordinates', {}).get('alt', ''),
                
                'gene': first_trans.get('gene', ''),
                # for now just be lazy and assume the first transcript consequence is the one we want
                'dna_change': first_trans.get('dna_change', ''),
                'consequence': first_trans.get('consequence', ''),
                'categories': ','.join(variant.get('categories', [])),
                'clinvar_significance': variant.get('clinvar_significance', ''),
                'date_of_phenotype_match': variant.get('date_of_phenotype_match', ''),
                'evidence_last_updated': variant.get('evidence_last_updated', ''),
                'first_tagged': variant.get('first_tagged', ''),
            }
            writer.writerow(row)
