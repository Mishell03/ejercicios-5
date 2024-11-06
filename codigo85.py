import streamlit as st
import pulp

st.title("Ejercicio 8.5: Problema de Asignación Binaria para Maximizar el NPV")

st.write("""
La empresa tiene seis proyectos de investigación y desarrollo (R&D) con un valor presente neto (NPV) estimado. 
El objetivo es seleccionar los proyectos que maximicen el NPV, considerando restricciones presupuestarias en cada año.
Cada proyecto es representado por una variable binaria que indica si el proyecto se selecciona o no.
""")

npv_proyectos = {"P1": 141, "P2": 187, "P3": 163, "P4": 153, "P5": 189, "P6": 127}
costos_por_ano = {
    "P1": [75, 25, 20, 15, 10],
    "P2": [90, 50, 25, 15, 10],
    "P3": [80, 60, 25, 15, 15],
    "P4": [40, 20, 15, 10, 10],
    "P5": [100, 30, 20, 10, 10],
    "P6": [50, 20, 10, 10, 10]
}
presupuestos = [250, 75, 50, 50, 50]

st.subheader("Datos del problema")

import pandas as pd
df_costos = pd.DataFrame(costos_por_ano).T
df_costos.columns = [f"Año {i+1}" for i in range(len(presupuestos))]
df_costos["NPV"] = [npv_proyectos[p] for p in npv_proyectos]
st.write("Costos de capital requeridos por año y NPV esperado para cada proyecto:")
st.dataframe(df_costos)

prob = pulp.LpProblem("Maximizar_NPV", pulp.LpMaximize)

proyectos = {p: pulp.LpVariable(p, cat="Binary") for p in npv_proyectos}

prob += pulp.lpSum(proyectos[p] * npv_proyectos[p] for p in npv_proyectos), "NPV_Total"

for i, presupuesto in enumerate(presupuestos):
    prob += pulp.lpSum(proyectos[p] * costos_por_ano[p][i] for p in npv_proyectos) <= presupuesto, f"Presupuesto_año_{i+1}"

prob.solve()

estado = pulp.LpStatus[prob.status]
valor_objetivo = pulp.value(prob.objective)

st.subheader("Resultados:")
st.write(f"Estado del problema: {estado}")
st.write(f"Valor óptimo de NPV: {valor_objetivo}")

st.write("Proyectos seleccionados:")
for p in proyectos:
    seleccion = "Seleccionado" if proyectos[p].varValue == 1 else "No seleccionado"
    st.write(f"{p}: {seleccion}")