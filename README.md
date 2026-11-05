# gauge-rr-crossed

## Français

Décomposer répétabilité et reproductibilité de mesures croisées.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m gauge_rr_crossed examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

ANOVA croisée équilibrée avec interaction opérateur×pièce ; conserve les composantes négatives avant troncature, contrairement à un simple écart-type global.

### Limites

Modèle aléatoire classique équilibré, sans intervalle de confiance ni verdict qualité automatique ; hypothèses et arrondis à examiner.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Decompose repeatability and reproducibility of crossed measurements.

Synthetic data; no network access or secret required.

```sh
python -m gauge_rr_crossed examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Balanced crossed ANOVA with operator×part interaction; retains negative components before truncation, unlike a global standard deviation.

### Limits

Classical balanced random-effects model, no confidence interval or automatic quality verdict; assumptions and rounding need review.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Descomponer repetibilidad y reproducibilidad de mediciones cruzadas.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m gauge_rr_crossed examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

ANOVA cruzado equilibrado con interacción operador×pieza; conserva componentes negativos antes del truncado, frente a desviación global.

### Límites

Modelo clásico equilibrado de efectos aleatorios, sin intervalo de confianza ni veredicto automático; revisar hipótesis y redondeo.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.nist.gov/publications/nistsematech-engineering-statistics-handbook-chapter-2-measurement-process
