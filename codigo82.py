import streamlit as st
import pulp
import time

st.title("Ejercicio 8.2: Tiempo de Cálculo para Problema LP")

st.write("""
Comparación del tiempo de cálculo entre el problema LP continuo y el problema LP con restricciones enteras.
""")

prob_lp = pulp.LpProblem("Maximizar_P_LP", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)

prob_lp += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
prob_lp += 4 * x1 + 2 * x2 + x3 <= 10, "Restricción 1"
prob_lp += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Restricción 2"
prob_lp += 2 * x1 + x2 + 3 * x3 <= 7, "Restricción 3"

start_time = time.time()
prob_lp.solve()
end_time = time.time()
tiempo_calculo_lp = end_time - start_time

estado_lp = pulp.LpStatus[prob_lp.status]
valor_objetivo_lp = pulp.value(prob_lp.objective)

st.subheader("Resultados para el problema LP continuo:")
st.write(f"Tiempo de cálculo: {tiempo_calculo_lp:.4f} segundos")
st.write(f"Estado del problema LP: {estado_lp}")
st.write(f"Valor óptimo de la función objetivo LP: {valor_objetivo_lp}")

st.write("Valores óptimos de las variables de decisión (LP continuo):")
for variable in prob_lp.variables():
    st.write(f"{variable.name} = {variable.varValue}")

prob_entero = pulp.LpProblem("Maximizar_P", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0, cat="Integer")
x2 = pulp.LpVariable("x2", lowBound=0, cat="Integer")
x3 = pulp.LpVariable("x3", lowBound=0, cat="Integer")

prob_entero += 4 * x1 + 3 * x2 + 3 * x3, "Función Objetivo"
prob_entero += 4 * x1 + 2 * x2 + x3 <= 10, "Restricción 1"
prob_entero += 3 * x1 + 4 * x2 + 2 * x3 <= 14, "Restricción 2"
prob_entero += 2 * x1 + x2 + 3 * x3 <= 7, "Restricción 3"

start_time = time.time()
prob_entero.solve()
end_time = time.time()
tiempo_calculo_entero = end_time - start_time

estado_entero = pulp.LpStatus[prob_entero.status]
valor_objetivo_entero = pulp.value(prob_entero.objective)

st.subheader("Resultados para el problema LP con restricciones enteras:")
st.write(f"Tiempo de cálculo: {tiempo_calculo_entero:.4f} segundos")
st.write(f"Estado del problema LP con enteros: {estado_entero}")
st.write(f"Valor óptimo de la función objetivo (Entero): {valor_objetivo_entero}")

st.write("Valores óptimos de las variables de decisión (LP con enteros):")
for variable in prob_entero.variables():
    st.write(f"{variable.name} = {variable.varValue}")