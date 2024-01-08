import os

init = 'step3_input'
mini_prefix = 'step4.0_minimization'
equi_prefix = 'step4.1_equilibration'
prod_prefix = 'step5_production'
prod_step   = 'step5'

os.system(f'gmx grompp -f {mini_prefix}.mdp -o {mini_prefix}.tpr -c {init}.gro -r {init}.gro -p topol.top -n index.ndx -maxwarn')
os.system(f'gmx mdrun -v -deffnm {mini_prefix} ')

os.system(f'gmx grompp -f {equi_prefix}.mdp -o {equi_prefix}.tpr -c {mini_prefix}.gro -r {init}.gro -p topol.top -n index.ndx -maxwarn')
os.system(f'gmx mdrun -v -deffnm {equi_prefix}')

os.system(f'gmx grompp -f {prod_prefix}.mdp -o final.tpr -c {equi_prefix}.gro -p topol.top -n index.ndx -maxwarn')
os.system(f'gmx mdrun -v -deffnm final')



