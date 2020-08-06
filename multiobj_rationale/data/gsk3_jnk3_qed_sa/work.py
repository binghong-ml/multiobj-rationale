from rdkit import Chem
import multiobj_rationale.scripts.sascorer as sascorer
from rdkit.Chem import Descriptors
import rdkit.Chem.QED as QED
import sys

for line in sys.stdin:
    rat, smiles = line.split()
    mol = Chem.MolFromSmiles(smiles)
    print(rat, smiles, QED.qed(mol), sascorer.calculateScore(mol), Descriptors.MolWt(mol))

