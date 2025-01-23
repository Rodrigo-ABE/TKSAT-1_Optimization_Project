import win32com.client

# Crear una instancia de STK
stk = win32com.client.Dispatch("STK11.Application")
stk.Visible = True  # Hace visible la ventana de STK
stk.UserControl = True

# Crear un nuevo escenario
stkRoot = stk.Personality2
stkRoot.NewScenario("DemoPython")
scenario = stkRoot.CurrentScenario

# Añadir un satélite al escenario
satellite = scenario.Children.New(18, "Satellite1")  # 18 es el tipo de objeto para satélite
satellite.PropagatorType = 2  # Usar propagación Kepleriana

# Configurar la órbita
keplerian = satellite.Propagator
keplerian.InitialState.Representation.AssignClassical(0, 7000, 0.001, 98, 0, 0, 0)  # Órbita
keplerian.Propagate()

print("Satélite creado y propagado.")
