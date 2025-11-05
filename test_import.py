print('=== TEST IMPORT ORBITAL MODULE ===') 
try: 
    from orbital_module.soi_core import SkyportOrbitalInterface 
    print('? Import berhasil') 
    soi = SkyportOrbitalInterface() 
    print('? Object created') 
    nodes = soi.simulate_orbital_nodes() 
    print('? Nodes simulated:', nodes) 
except Exception as e: 
    print('? Error:', e) 
    import traceback 
    traceback.print_exc() 
