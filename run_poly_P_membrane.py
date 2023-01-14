import os

init = 'step5_input'
rest_prefix = 'step5_input'
mini_prefix = 'step6.0_minimization'
equi_prefix = f'step6.{}_equilibration'
prod_prefix = 'step7_production'
prod_step   = 'final


# Minimization

os.system(f'gmx grompp -f {mini_prefix}.mdp -o {mini_prefix}.tpr -c {init}.gro -r {rest_prefix}.gro -p topol.top -n index.ndx -maxwarn -1')
os.system(f'gmx_d mdrun -v -deffnm {mini_prefix}')


# Equilibration
for i in range(6):
    c = i+1
    istep = f'step6.{c}_equilibration'
    pstep = f'step6.{c-1}_equilibration'
    if c==1:
        pstep = mini_prefix

    os.system(f'gmx grompp -f {istep}.mdp -o {istep}.tpr -c {pstep}.gro -r {rest_prefix}.gro -p topol.top -n index.ndx -maxwarn -1')
    os.system(f'gmx mdrun -v -deffnm {istep}')

    
# Production run 
os.system(f'gmx grompp -f {prod_prefix}.mdp -o final.tpr -c step6.6_equilibration.gro -p topol.top -n index.ndx -maxwarn -1')
os.system(f'gmx mdrun -v -deffnm final')


