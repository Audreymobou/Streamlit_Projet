"""
Dashboard Premier League 2019-2024
Audience : direction sportive d'un club professionnel
Lancement : streamlit run app.py
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# =============================================================================
# 1. Configuration
# =============================================================================
st.set_page_config(
    page_title="La victoire ne dépend pas seulement du terrain",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_DIR = Path(__file__).parent / "data"
DATA_DIR.mkdir(exist_ok=True)

SEASONS = {
    "2019-20": "1920",
    "2020-21": "2021",
    "2021-22": "2122",
    "2022-23": "2223",
    "2023-24": "2324",
}
SEASON_ORDER = list(SEASONS.keys())
BASELINE_SEASON = "2019-20"

NEEDED_COLS = [
    "Div", "Date", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "FTR",
    "HTHG", "HTAG", "HTR", "Referee", "HS", "AS", "HST", "AST",
    "HF", "AF", "HC", "AC", "HY", "AY", "HR", "AR",
]

THEME = {
    "navy": "#0A1B33",
    "navy_2": "#122C4E",
    "green": "#0EA894",
    "green_dark": "#0A7F6E",
    "green_soft": "#E6F7F4",
    "gold": "#C9992F",
    "red": "#EC7412",
    "blue": "#3D64C4",
    "slate": "#5B6B7E",
    "text": "#101B2E",
    "muted": "#64748B",
    "background": "#F4F6FA",
    "surface": "#FFFFFF",
    "border": "#E3E7EF",
    "grid": "#EEF1F6",
}

PLOTLY_CONFIG = {
    "displayModeBar": False,
    "responsive": True,
    "scrollZoom": False,
}

# =============================================================================
# 2. Design system
# =============================================================================
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

    :root {{
        --navy: {THEME['navy']};
        --navy-2: {THEME['navy_2']};
        --green: {THEME['green']};
        --green-dark: {THEME['green_dark']};
        --gold: {THEME['gold']};
        --surface: {THEME['surface']};
        --border: {THEME['border']};
        --text: {THEME['text']};
        --muted: {THEME['muted']};
    }}

    html, body, [class*="css"] {{
        font-family: "Inter", ui-sans-serif, system-ui, -apple-system,
                     BlinkMacSystemFont, "Segoe UI", sans-serif;
    }}

    .stApp {{
        background:
            radial-gradient(circle at 90% 0%, rgba(14,168,148,.08), transparent 30rem),
            radial-gradient(circle at 5% 100%, rgba(11,31,51,.05), transparent 30rem),
            {THEME['background']};
        color: var(--text);
    }}

    .block-container {{
        max-width: 1360px;
        margin: 0 auto;
        padding: 1.4rem 2.4rem 3.4rem;
    }}

    #MainMenu, footer {{ visibility: hidden; }}
    header[data-testid="stHeader"] {{ background: transparent; }}

    h1, h2, h3 {{
        color: var(--navy) !important;
        letter-spacing: -.025em;
        font-weight: 800 !important;
    }}
    h1 {{ font-size: 1.9rem !important; line-height: 1.15 !important; }}
    h2 {{ font-size: 1.28rem !important; }}
    h3 {{ font-size: 1.02rem !important; }}
    p, li, label {{ font-size: .87rem !important; line-height: 1.55 !important; }}
    [data-testid="stCaptionContainer"] p {{
        color: var(--muted) !important;
        font-size: .74rem !important;
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(195deg, {THEME['navy']} 0%, {THEME['navy_2']} 100%);
        border-right: 0;
        box-shadow: 6px 0 28px rgba(7,20,35,.14);
    }}
    section[data-testid="stSidebar"] > div {{ padding-top: 1.3rem; }}
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] label {{ color: white !important; }}
    section[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {{
        color: rgba(255,255,255,.58) !important;
    }}
    section[data-testid="stSidebar"] [data-baseweb="select"] > div,
    section[data-testid="stSidebar"] [data-baseweb="base-input"] {{
        background: rgba(255,255,255,.07) !important;
        border-color: rgba(255,255,255,.16) !important;
        border-radius: 10px !important;
    }}
    section[data-testid="stSidebar"] [role="radiogroup"] label {{
        background: rgba(255,255,255,.05);
        border: 1px solid rgba(255,255,255,.1);
        border-radius: 9px;
        padding: .4rem .6rem;
        margin-bottom: .3rem;
        transition: background .15s ease;
    }}
    section[data-testid="stSidebar"] [role="radiogroup"] label:hover {{
        background: rgba(255,255,255,.1);
    }}

    /* ---- KPI cards : grandes, centrées, premium ---- */
    [data-testid="stMetric"] {{
        min-height: 172px;
        padding: 1.5rem 1.4rem 1.35rem;
        background: linear-gradient(180deg, rgba(255,255,255,1) 0%, rgba(252,253,254,1) 100%);
        border: 1px solid var(--border);
        border-top: none;
        border-radius: 18px;
        box-shadow: 0 10px 28px rgba(7,27,46,.06);
        transition: transform .2s ease, box-shadow .2s ease;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        position: relative;
    }}
    [data-testid="stMetric"]::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        border-radius: 18px 18px 0 0;
        background: linear-gradient(90deg, var(--green) 0%, {THEME['gold']} 100%);
    }}
    [data-testid="stMetric"]:hover {{
        transform: translateY(-3px);
        box-shadow: 0 16px 36px rgba(7,27,46,.1);
    }}
    [data-testid="stMetric"] > div {{
        align-items: center !important;
        justify-content: center !important;
        width: 100%;
    }}
    [data-testid="stMetricLabel"] {{
        justify-content: center !important;
        width: 100%;
    }}
    [data-testid="stMetricLabel"] p {{
        color: var(--muted) !important;
        font-size: .78rem !important;
        font-weight: 700 !important;
        letter-spacing: .05em;
        text-transform: uppercase;
        text-align: center;
        width: 100%;
    }}
    [data-testid="stMetricValue"] {{
        color: var(--navy) !important;
        font-size: 2.7rem !important;
        font-weight: 850 !important;
        letter-spacing: -.04em;
        text-align: center;
        justify-content: center !important;
        width: 100%;
        margin: .25rem 0 .1rem;
    }}
    [data-testid="stMetricDelta"] {{
        font-size: .76rem !important;
        justify-content: center !important;
        width: 100%;
    }}
    [data-testid="stMetricDelta"] > div {{ justify-content: center !important; }}

    [data-baseweb="tab-list"] {{
        gap: .35rem;
        padding: .34rem;
        background: white;
        border: 1px solid var(--border);
        border-radius: 14px;
        box-shadow: 0 4px 14px rgba(7,27,46,.04);
        justify-content: center;
    }}
    button[data-baseweb="tab"] {{
        height: 42px;
        padding: 0 1.05rem !important;
        border-radius: 10px;
        color: var(--muted);
        font-size: .8rem !important;
        font-weight: 650;
        transition: background .15s ease, color .15s ease;
    }}
    button[data-baseweb="tab"]:hover {{
        background: {THEME['green_soft']};
        color: var(--green-dark) !important;
    }}
    button[data-baseweb="tab"][aria-selected="true"] {{
        color: white !important;
        background: linear-gradient(135deg, var(--navy) 0%, var(--navy-2) 100%) !important;
        box-shadow: 0 6px 16px rgba(11,31,51,.22);
    }}
    button[data-baseweb="tab"][aria-selected="true"]:hover {{
        color: white !important;
    }}
    [data-baseweb="tab-highlight"], [data-baseweb="tab-border"] {{ display: none; }}

    [data-testid="stPlotlyChart"], [data-testid="stDataFrame"] {{
        background: white;
        border: 1px solid var(--border);
        border-radius: 16px;
        box-shadow: 0 8px 24px rgba(7,27,46,.045);
        overflow: hidden;
    }}
    [data-testid="stPlotlyChart"] {{ padding: .4rem; }}
    [data-testid="stAlert"] {{ border-radius: 12px; }}
    hr {{ border-color: var(--border) !important; margin: 1.4rem 0 !important; }}

    ::-webkit-scrollbar {{ width: 9px; height: 9px; }}
    ::-webkit-scrollbar-track {{ background: transparent; }}
    ::-webkit-scrollbar-thumb {{ background: rgba(11,31,51,.18); border-radius: 6px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: rgba(11,31,51,.32); }}

    @media (max-width: 900px) {{
        .block-container {{ padding: 1rem; }}
        h1 {{ font-size: 1.55rem !important; }}
        [data-testid="stMetric"] {{ min-height: 140px; padding: 1.1rem; }}
        [data-testid="stMetricValue"] {{ font-size: 2.1rem !important; }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


def render_brand():
    st.sidebar.markdown(
        f"""
        <div style="padding:0 0 1.15rem;border-bottom:1px solid rgba(255,255,255,.13);margin-bottom:1.2rem">
          <div style="display:flex;align-items:center;gap:.7rem">
            <div style="width:38px;height:38px;border-radius:11px;background:{THEME['green']};
                        display:flex;align-items:center;justify-content:center;color:white;
                        font-size:1.05rem;box-shadow:0 8px 18px rgba(14,168,148,.32)">◆</div>
            <div>
              <div style="color:white;font-size:.94rem;font-weight:750;line-height:1.15">Performance Lab</div>
              <div style="color:rgba(255,255,255,.52);font-size:.62rem;letter-spacing:.13em;
                          text-transform:uppercase;margin-top:.18rem">Sports Intelligence</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_header():
    st.markdown(
        f"""
        <div style="position:relative;overflow:hidden;margin-bottom:1.05rem;padding:1.65rem 1.85rem;
                    border-radius:20px;color:white;background:radial-gradient(circle at 88% 15%,
                    rgba(14,168,148,.42),transparent 31%),linear-gradient(125deg,{THEME['navy']} 0%,
                    {THEME['navy_2']} 100%);box-shadow:0 16px 40px rgba(7,27,46,.13)">
          <div style="color:#7FE3CB;font-size:.66rem;font-weight:750;letter-spacing:.14em;
                      text-transform:uppercase;margin-bottom:.65rem">Premier League · 2019–2024</div>
          <div style="max-width:920px;font-size:clamp(1.45rem,2.4vw,2.15rem);font-weight:780;
                      line-height:1.14;letter-spacing:-.04em;margin-bottom:.62rem">
            Quels sont les éléments qui influencent les performances des équipes?
          </div>
          <div style="max-width:850px;color:rgba(255,255,255,.74);font-size:.86rem;line-height:1.55">
            Dominer le jeu, convertir ses occasions et maîtriser le risque disciplinaire
            sont les trois leviers observés de la performance.
          </div>
          <div style="display:inline-flex;margin-top:.95rem;padding:.42rem .72rem;border-radius:999px;
                      border:1px solid rgba(255,255,255,.15);background:rgba(255,255,255,.07);
                      color:rgba(255,255,255,.82);font-size:.68rem;font-weight:650">
            Note stratégique · Direction sportive
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_intro(eyebrow, title, description):
    st.markdown(
        f"""
        <div style="margin:.65rem 0 .9rem">
          <div style="color:{THEME['green_dark']};font-size:.64rem;font-weight:750;letter-spacing:.12em;
                      text-transform:uppercase;margin-bottom:.25rem">{eyebrow}</div>
          <div style="color:{THEME['navy']};font-size:1.18rem;font-weight:750;
                      letter-spacing:-.025em;margin-bottom:.25rem">{title}</div>
          <div style="max-width:900px;color:{THEME['muted']};font-size:.8rem;line-height:1.5">{description}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def insight_card(title, text, accent=None):
    accent = accent or THEME["green"]
    st.markdown(
        f"""
        <div style="margin:.85rem 0;padding:.9rem 1rem;background:white;border:1px solid {THEME['border']};
                    border-left:4px solid {accent};border-radius:13px;box-shadow:0 5px 18px rgba(7,27,46,.04)">
          <div style="color:{THEME['navy']};font-size:.79rem;font-weight:750;margin-bottom:.23rem">{title}</div>
          <div style="color:{THEME['muted']};font-size:.76rem;line-height:1.52">{text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def style_figure(fig, height=410, legend=True):
    fig.update_layout(
        height=height,
        template="plotly_white",
        font=dict(family="Inter, Arial, sans-serif", size=11, color=THEME["text"]),
        title=dict(x=.025, xanchor="left", y=.96, yanchor="top",
                   font=dict(size=13, color=THEME["navy"])),
        margin=dict(l=55, r=28, t=78, b=48),
        paper_bgcolor=THEME["surface"],
        plot_bgcolor=THEME["surface"],
        hoverlabel=dict(bgcolor=THEME["navy"], bordercolor=THEME["navy"],
                        font=dict(color="white", size=11)),
        legend=dict(visible=legend, orientation="h", yanchor="bottom", y=1.02,
                    xanchor="right", x=1, font=dict(size=10, color=THEME["muted"]),
                    title_font=dict(size=10), bgcolor="rgba(0,0,0,0)"),
    )
    fig.update_xaxes(
        showline=False, zeroline=False, gridcolor=THEME["grid"],
        tickfont=dict(size=10, color=THEME["muted"]),
        title_font=dict(size=10, color=THEME["muted"]),
        title_standoff=12, automargin=True,
    )
    fig.update_yaxes(
        showline=False, zeroline=False, gridcolor=THEME["grid"],
        tickfont=dict(size=10, color=THEME["muted"]),
        title_font=dict(size=10, color=THEME["muted"]),
        title_standoff=12, automargin=True,
    )
    return fig

# =============================================================================
# 3. Données
# =============================================================================
@st.cache_data(show_spinner="Chargement des données Premier League...")
def load_matches():
    frames, missing = [], []
    for label, code in SEASONS.items():
        local_path = DATA_DIR / f"E0_{code}.csv"
        df_season = None
        if local_path.exists():
            for encoding in ("utf-8", "latin1"):
                try:
                    df_season = pd.read_csv(local_path, encoding=encoding)
                    break
                except Exception:
                    pass
        if df_season is None:
            url = f"https://www.football-data.co.uk/mmz4281/{code}/E0.csv"
            try:
                df_season = pd.read_csv(url, encoding="latin1")
                df_season.to_csv(local_path, index=False)
            except Exception:
                missing.append(label)
                continue
        df_season["Season"] = label
        frames.append(df_season)

    if missing:
        st.warning(
            "Saisons non chargées : " + ", ".join(missing) +
            ". Ajoutez les fichiers correspondants dans le dossier data/."
        )
    if not frames:
        st.error(
            "Aucune donnée disponible. Placez les CSV E0 dans data/ ou relancez "
            "l'application avec une connexion internet."
        )
        st.stop()

    raw = pd.concat(frames, ignore_index=True)
    cols = [c for c in NEEDED_COLS + ["Season"] if c in raw.columns]
    df = raw[cols].copy()
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")
    df = df.dropna(subset=["HomeTeam", "AwayTeam", "FTR"])
    numeric_cols = [
        "FTHG", "FTAG", "HS", "AS", "HST", "AST", "HF", "AF",
        "HC", "AC", "HY", "AY", "HR", "AR",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df["Season"] = pd.Categorical(df["Season"], categories=SEASON_ORDER, ordered=True)
    return df


@st.cache_data(show_spinner=False)
def build_team_matches(df):
    def make_side(venue, team_col, opp_col, gf_col, ga_col, win_code):
        d = df.copy()
        d["Team"] = d[team_col]
        d["Opponent"] = d[opp_col]
        d["Venue"] = venue
        d["GF"] = d[gf_col]
        d["GA"] = d[ga_col]
        mapping = {
            "Shots": "HS" if venue == "Domicile" else "AS",
            "ShotsOnTarget": "HST" if venue == "Domicile" else "AST",
            "Corners": "HC" if venue == "Domicile" else "AC",
            "Fouls": "HF" if venue == "Domicile" else "AF",
            "Yellow": "HY" if venue == "Domicile" else "AY",
            "Red": "HR" if venue == "Domicile" else "AR",
        }
        for target, source in mapping.items():
            d[target] = d[source] if source in d.columns else pd.NA
        d["Points"] = d["FTR"].map(lambda r: 3 if r == win_code else (1 if r == "D" else 0))
        d["Result"] = d["FTR"].map(
            lambda r: "Victoire" if r == win_code else ("Nul" if r == "D" else "Défaite")
        )
        return d

    home = make_side("Domicile", "HomeTeam", "AwayTeam", "FTHG", "FTAG", "H")
    away = make_side("Extérieur", "AwayTeam", "HomeTeam", "FTAG", "FTHG", "A")
    keep = [
        "Season", "Date", "Team", "Opponent", "Venue", "GF", "GA", "Shots",
        "ShotsOnTarget", "Corners", "Fouls", "Yellow", "Red", "Points", "Result",
    ]
    if "Referee" in home.columns:
        keep.append("Referee")
    result = pd.concat([home[keep], away[keep]], ignore_index=True)
    result["Season"] = pd.Categorical(result["Season"], categories=SEASON_ORDER, ordered=True)
    return result

# =============================================================================
# 4. Indicateurs
# =============================================================================
def home_away_ppg_gap(team_df):
    means = team_df.groupby("Venue", observed=True)["Points"].mean()
    if not {"Domicile", "Extérieur"}.issubset(means.index):
        return float("nan")
    return means["Domicile"] - means["Extérieur"]


def conversion_rate(team_df):
    shots = team_df["ShotsOnTarget"].sum(min_count=1)
    goals = team_df["GF"].sum(min_count=1)
    return goals / shots * 100 if pd.notna(shots) and shots > 0 else float("nan")


def discipline_index(team_df):
    if team_df.empty:
        return float("nan")
    return (team_df["Yellow"].fillna(0) + 2 * team_df["Red"].fillna(0)).mean()


def fmt_delta(value, baseline, suffix=""):
    if pd.isna(value) or pd.isna(baseline):
        return "Référence indisponible"
    return f"{value - baseline:+.2f}{suffix} vs 2019-20"

# =============================================================================
# 5. Chargement et filtres
# =============================================================================
matches = load_matches()
team_matches = build_team_matches(matches)

render_brand()
st.sidebar.markdown(
    "<div style='color:rgba(255,255,255,.55);font-size:.63rem;font-weight:750;"
    "letter-spacing:.12em;text-transform:uppercase;margin-bottom:.7rem'>"
    "Périmètre d'analyse</div>",
    unsafe_allow_html=True,
)

selected_seasons = st.sidebar.multiselect(
    "Saisons",
    options=SEASON_ORDER,
    default=SEASON_ORDER,
)
selected_teams = st.sidebar.multiselect(
    "Équipes",
    options=sorted(team_matches["Team"].dropna().unique()),
    default=[],
    placeholder="Toutes les équipes",
)
venue_choice = st.sidebar.radio(
    "Lieu",
    options=["Tous", "Domicile", "Extérieur"],
    index=0,
)

st.sidebar.divider()
st.sidebar.caption(
    "Source : football-data.co.uk · Division E0 · Saisons 2019/20 à 2023/24."
)

if not selected_seasons:
    st.warning("Sélectionnez au moins une saison dans la barre latérale.")
    st.stop()

scope_all_venues = team_matches[team_matches["Season"].isin(selected_seasons)].copy()
if selected_teams:
    scope_all_venues = scope_all_venues[scope_all_venues["Team"].isin(selected_teams)]

filtered = scope_all_venues.copy()
if venue_choice != "Tous":
    filtered = filtered[filtered["Venue"] == venue_choice]

matches_filtered = matches[matches["Season"].isin(selected_seasons)].copy()

if filtered.empty:
    st.warning("Aucune rencontre ne correspond aux filtres sélectionnés.")
    st.stop()

baseline_all = team_matches[team_matches["Season"] == BASELINE_SEASON].copy()
if selected_teams:
    baseline_all = baseline_all[baseline_all["Team"].isin(selected_teams)]
baseline_filtered = baseline_all.copy()
if venue_choice != "Tous":
    baseline_filtered = baseline_filtered[baseline_filtered["Venue"] == venue_choice]

# =============================================================================
# 6. Vue exécutive
# =============================================================================
render_header()

kpi_gap = home_away_ppg_gap(scope_all_venues)
kpi_conversion = conversion_rate(filtered)
kpi_discipline = discipline_index(filtered)
base_gap = home_away_ppg_gap(baseline_all)
base_conversion = conversion_rate(baseline_filtered)
base_discipline = discipline_index(baseline_filtered)

c1, c2, c3 = st.columns(3, gap="large")
c1.metric(
    "Avantage domicile",
    "N/D" if pd.isna(kpi_gap) else f"{kpi_gap:+.2f} pt/match",
    delta=fmt_delta(kpi_gap, base_gap),
    help="Écart moyen de points par match entre domicile et extérieur. Le filtre de lieu n'est pas appliqué à ce KPI.",
)
c2.metric(
    "Conversion des tirs cadrés",
    "N/D" if pd.isna(kpi_conversion) else f"{kpi_conversion:.1f} %",
    delta=fmt_delta(kpi_conversion, base_conversion, " pt"),
    help="Buts divisés par tirs cadrés sur le périmètre sélectionné.",
)
c3.metric(
    "Indice disciplinaire",
    "N/D" if pd.isna(kpi_discipline) else f"{kpi_discipline:.2f} / match",
    delta=fmt_delta(kpi_discipline, base_discipline),
    delta_color="inverse",
    help="Cartons jaunes + 2 × cartons rouges, par équipe et par match.",
)
st.caption(
    "Comparaison avec 2019-20. L'avantage domicile est calculé sur les deux lieux afin de préserver la comparabilité."
)

st.divider()

# =============================================================================
# 7. Analyses détaillées
# =============================================================================
tab1, tab2, tab3, tab4 = st.tabs([
    " Avantage domicile",
    " Efficacité offensive",
    " Discipline",
    " Classement",
])

with tab1:
    section_intro(
        "Avantage compétitif",
        "Il existe d'autres critères de performance hormis le match à domicile",
        "Certes, jouer à domicile impacte les résultats mais pas que au vu de l'évolution des résultats par saison ",
    )

    per_season = (
        scope_all_venues.groupby(["Season", "Venue"], observed=True)["Points"]
        .mean().unstack("Venue").reindex(selected_seasons).reset_index()
        .rename(columns={"Domicile": "PPG Domicile", "Extérieur": "PPG Extérieur"})
    )
    fig1 = px.bar(
        per_season,
        x="Season",
        y=[c for c in ["PPG Domicile", "PPG Extérieur"] if c in per_season.columns],
        barmode="group",
        color_discrete_map={
            "PPG Domicile": THEME["green"],
            "PPG Extérieur": THEME["navy_2"],
        },
        labels={"value": "Points par match", "Season": "Saison", "variable": "Lieu"},
        title="Points par match selon le lieu",
    )
    fig1.update_traces(marker_line_width=0,
                       hovertemplate="<b>Saison : %{x}</b><br>Points par match : %{y:.2f}<extra></extra>")
    fig1.update_yaxes(gridcolor=THEME["grid"])
    st.plotly_chart(style_figure(fig1, 395), use_container_width=True, config=PLOTLY_CONFIG)

    season_match_scope = matches_filtered.copy()
    if selected_teams:
        season_match_scope = season_match_scope[
            season_match_scope["HomeTeam"].isin(selected_teams) |
            season_match_scope["AwayTeam"].isin(selected_teams)
        ]
    valid_shots = season_match_scope.dropna(subset=["HST", "AST"])
    if not valid_shots.empty:
        selected_at_home = valid_shots if not selected_teams else valid_shots[valid_shots["HomeTeam"].isin(selected_teams)]
        if not selected_at_home.empty:
            dominates = selected_at_home["HST"] > selected_at_home["AST"]
            with_dom = (selected_at_home.loc[dominates, "FTR"] == "H").mean() * 100 if dominates.any() else float("nan")
            without_dom = (selected_at_home.loc[~dominates, "FTR"] == "H").mean() * 100 if (~dominates).any() else float("nan")
            if pd.notna(with_dom) and pd.notna(without_dom):
                insight_card(
                    "Commentaire",
                    f"Quand l'équipe observée à domicile cadre davantage que son adversaire, elle gagne <strong>{with_dom:.1f} %</strong> de ses matchs, contre <strong>{without_dom:.1f} %</strong> sinon. Cette association favorise la domination sans conluire à une causalité.",
                )

with tab2:
    section_intro(
        "Performance offensive",
        "Plus une équipe est offensive, mieux sont son taux de conversion et son nombre de points",
        ".On gagne en concrétisant nos tirs cadrés en but",
    )

    team_off = (
        filtered.groupby("Team", observed=True)
        .agg(Matchs=("GF", "count"), Buts=("GF", "sum"),
             TirsCadres=("ShotsOnTarget", "sum"), Points=("Points", "sum"))
        .reset_index()
    )
    team_off = team_off[(team_off["Matchs"] >= 5) & (team_off["TirsCadres"] > 0)].copy()
    team_off["Conversion (%)"] = team_off["Buts"].div(team_off["TirsCadres"]).mul(100)
    team_off["Points/Match"] = team_off["Points"].div(team_off["Matchs"])

    if team_off.empty:
        st.info("Pas assez de matchs pour calculer les indicateurs offensifs sur ce périmètre.")
    else:
        left, right = st.columns([.92, 1.08], gap="medium")
        with left:
            # Mise en valeur des deux extrêmes du Top 12 : meilleure et plus faible conversion.
            # En cas d'égalité, toutes les équipes partageant l'extrême sont colorées.
            top = team_off.nlargest(12, "Conversion (%)").sort_values("Conversion (%)").copy()
            max_conversion = top["Conversion (%)"].max()
            min_conversion = top["Conversion (%)"].min()

            top["Niveau"] = "Intermédiaire"
            top.loc[top["Conversion (%)"] == max_conversion, "Niveau"] = "Maximum"
            top.loc[top["Conversion (%)"] == min_conversion, "Niveau"] = "Minimum"

            # Afficher la valeur de conversion sur toutes les barres.
            top["Étiquette"] = top["Conversion (%)"].map(lambda value: f"{value:.1f} %")

            fig2a = px.bar(
                top,
                x="Conversion (%)",
                y="Team",
                orientation="h",
                color="Niveau",
                text="Étiquette",
                title="les meilleures équipes ont un taux de conversion croissant ",
                labels={
                    "Team": "",
                    "Conversion (%)": "Taux de conversion (%)",
                    "Niveau": "",
                },
                color_discrete_map={
                    "Maximum": THEME["green"],
                    "Intermédiaire": "#DBE1E9",
                    "Minimum": THEME["red"],
                },
                category_orders={
                    "Niveau": ["Maximum", "Intermédiaire", "Minimum"],
                },
            )
            fig2a.update_traces(
                marker_line_width=0,
                textposition="outside",
                textfont=dict(size=10, color=THEME["navy"]),
                textangle=0,
                cliponaxis=False,
                hovertemplate=(
                    "<b>Équipe : %{y}</b><br>"
                    "Taux de conversion : %{x:.1f} %<extra></extra>"
                ),
            )
            fig2a.update_xaxes(
                showgrid=False,
                range=[0, max_conversion * 1.16],
            )
            fig2a.update_yaxes(
                gridcolor="rgba(0,0,0,0)",
                categoryorder="array",
                categoryarray=top["Team"].tolist(),
            )
            st.plotly_chart(
                style_figure(fig2a, 470, True),
                use_container_width=True,
                config=PLOTLY_CONFIG,
            )

        with right:
            mean_conv = team_off["Conversion (%)"].mean()
            mean_ppg = team_off["Points/Match"].mean()
            fig2b = px.scatter(
                team_off, x="Conversion (%)", y="Points/Match", size="Matchs",
                hover_name="Team", color="Points/Match",
                color_continuous_scale=[[0, "#D7E0E8"], [.5, "#4FBBA5"], [1, THEME["green_dark"]]],
                title="Le nombre de points par match augmente avec l'augmentation du taux de conversion",
                labels={"Conversion (%)": "Taux de conversion (%)", "Points/Match": "Points par match", "Matchs": "Matchs joués"},
            )
            fig2b.add_vline(x=mean_conv, line_width=1, line_dash="dot", line_color=THEME["slate"])
            fig2b.add_hline(y=mean_ppg, line_width=1, line_dash="dot", line_color=THEME["slate"])
            fig2b.update_traces(
                marker=dict(opacity=.86, line=dict(width=1.5, color="white")),
                hovertemplate="<b>%{hovertext}</b><br>Taux de conversion : %{x:.1f} %<br>Points par match : %{y:.2f}<extra></extra>",
            )
            fig2b.update_layout(coloraxis_showscale=False)
            st.plotly_chart(style_figure(fig2b, 470, False), use_container_width=True, config=PLOTLY_CONFIG)

        corr = team_off["Conversion (%)"].corr(team_off["Points/Match"])
        insight_card(
            "Interprétation",
            f"La corrélation entre conversion et points par match est de <strong>{corr:.2f}</strong> sur le périmètre retenu. Le graphique décrit une association statistique et non une relation causale.",
            THEME["blue"],
        )

with tab3:
    section_intro(
        "Maîtrise du risque",
        "Moins de fautes peut favoriser un bon score",
        "L'indice disciplinaire combine cartons jaunes et rouges. Il sert à repérer les profils d'équipe exposés aux sanctions, expulsions et suspensions.",
    )

    team_disc = (
        filtered.groupby("Team", observed=True)
        .agg(Matchs=("GF", "count"), Jaunes=("Yellow", "sum"),
             Rouges=("Red", "sum"), Points=("Points", "sum"))
        .reset_index()
    )
    team_disc = team_disc[team_disc["Matchs"] >= 5].copy()
    team_disc["Cartons/Match"] = (team_disc["Jaunes"] + 2 * team_disc["Rouges"]) / team_disc["Matchs"]
    team_disc["Points/Match"] = team_disc["Points"] / team_disc["Matchs"]

    if team_disc.empty:
        st.info("Pas assez de matchs pour calculer l'indice disciplinaire sur ce périmètre.")
    else:
        mean_cards = team_disc["Cartons/Match"].mean()
        mean_points = team_disc["Points/Match"].mean()
        fig3 = px.scatter(
            team_disc, x="Cartons/Match", y="Points/Match", size="Matchs",
            hover_name="Team", color="Cartons/Match",
            color_continuous_scale=[[0, THEME["green"]], [.55, THEME["gold"]], [1, THEME["red"]]],
            title="Exposition disciplinaire et performance",
            labels={"Cartons/Match": "Indice disciplinaire par match", "Points/Match": "Points par match", "Matchs": "Matchs joués"},
            trendline="ols",
        )
        fig3.add_vline(x=mean_cards, line_width=1, line_dash="dot", line_color=THEME["slate"])
        fig3.add_hline(y=mean_points, line_width=1, line_dash="dot", line_color=THEME["slate"])
        fig3.update_traces(
            marker=dict(opacity=.84, line=dict(width=1.4, color="white")),
            hovertemplate="<b>%{hovertext}</b><br>Indice disciplinaire : %{x:.2f}<br>Points par match : %{y:.2f}<extra></extra>",
        )
        fig3.update_layout(coloraxis_showscale=False)
        st.plotly_chart(style_figure(fig3, 455, False), use_container_width=True, config=PLOTLY_CONFIG)

        corr_disc = team_disc["Cartons/Match"].corr(team_disc["Points/Match"])
        insight_card(
            "Intèprétation",
            f"La corrélation observée est de <strong>{corr_disc:.2f}</strong>. Une valeur proche de zéro traduit une association linéaire faible. Les cartons peuvent aussi refléter le style de jeu, le contexte du match et les décisions arbitrales.",
            THEME["gold"],
        )
        st.caption("Indice disciplinaire interne = cartons jaunes + 2 × cartons rouges, par équipe et par match.")

with tab4:
    section_intro(
        "Benchmark de performance",
        "Positionner les équipes dans leur environnement compétitif",
        "Le tableau compare résultats, production offensive et différence de buts. Si un lieu est sélectionné, il s'agit d'une vue de performance et non du classement officiel.",
    )

    season_for_ranking = st.selectbox(
        "Saison analysée",
        options=[s for s in SEASON_ORDER if s in selected_seasons],
    )
    rank_scope = team_matches[team_matches["Season"] == season_for_ranking].copy()
    if venue_choice != "Tous":
        rank_scope = rank_scope[rank_scope["Venue"] == venue_choice]

    ranking = (
        rank_scope.groupby("Team", observed=True)
        .agg(J=("GF", "count"), V=("Result", lambda s: (s == "Victoire").sum()),
             N=("Result", lambda s: (s == "Nul").sum()),
             D=("Result", lambda s: (s == "Défaite").sum()),
             BM=("GF", "sum"), BE=("GA", "sum"), Pts=("Points", "sum"))
        .reset_index().rename(columns={"Team": "Équipe"})
    )
    ranking["Diff"] = ranking["BM"] - ranking["BE"]
    ranking = ranking.sort_values(["Pts", "Diff", "BM"], ascending=False).reset_index(drop=True)
    ranking.insert(0, "Rang", ranking.index + 1)

    label = "Classement complet" if venue_choice == "Tous" else f"Performance {venue_choice.lower()}"
    st.markdown(f"**{label} · {season_for_ranking}**")
    st.dataframe(
        ranking[["Rang", "Équipe", "J", "V", "N", "D", "BM", "BE", "Diff", "Pts"]],
        use_container_width=True, hide_index=True,
        column_config={
            "Rang": st.column_config.NumberColumn("#", width="small"),
            "Équipe": st.column_config.TextColumn("Équipe", width="medium"),
            "Pts": st.column_config.NumberColumn("Pts", format="%d"),
        },
    )

    # Mise en valeur des deux extrêmes : maximum et minimum de points.
    # En cas d'égalité, toutes les équipes partageant l'extrême sont colorées.
    ranking_chart = ranking.sort_values("Pts", ascending=True).copy()
    max_points = ranking_chart["Pts"].max()
    min_points = ranking_chart["Pts"].min()

    ranking_chart["Niveau"] = "Intermédiaire"
    ranking_chart.loc[ranking_chart["Pts"] == max_points, "Niveau"] = "Maximum"
    ranking_chart.loc[ranking_chart["Pts"] == min_points, "Niveau"] = "Minimum"

    ranking_chart["Étiquette"] = ranking_chart.apply(
        lambda row: f"{int(row['Pts'])} pts" if row["Niveau"] != "Intermédiaire" else "",
        axis=1,
    )

    fig4 = px.bar(
        ranking_chart,
        x="Pts",
        y="Équipe",
        orientation="h",
        color="Niveau",
        text="Étiquette",
        title=f"{label} en points · {season_for_ranking}",
        labels={"Équipe": "Équipe", "Pts": "Points", "Niveau": "Niveau"},
        color_discrete_map={
            "Maximum": THEME["green"],
            "Intermédiaire": "#DBE1E9",
            "Minimum": THEME["red"],
        },
        category_orders={
            "Niveau": ["Maximum", "Intermédiaire", "Minimum"],
        },
    )

    fig4.update_traces(
        marker_line_width=0,
        textposition="outside",
        textfont=dict(size=10, color=THEME["navy"]),
        textangle=0,
        cliponaxis=False,
        hovertemplate=(
            "<b>Équipe : %{y}</b><br>"
            "Points : %{x:.0f}<extra></extra>"
        ),
    )
    fig4.update_xaxes(showgrid=False, range=[0, max_points * 1.12])
    fig4.update_yaxes(
        gridcolor="rgba(0,0,0,0)",
        categoryorder="array",
        categoryarray=ranking_chart["Équipe"].tolist(),
    )

    st.plotly_chart(
        style_figure(fig4, 560, True),
        use_container_width=True,
        config=PLOTLY_CONFIG,
    )

    best_teams = ", ".join(
        ranking_chart.loc[ranking_chart["Pts"] == max_points, "Équipe"].astype(str)
    )
    lowest_teams = ", ".join(
        ranking_chart.loc[ranking_chart["Pts"] == min_points, "Équipe"].astype(str)
    )
    insight_card(
        "Les deux extrêmes du classement",
        f"<strong>{best_teams}</strong> représente le maximum avec "
        f"<strong>{int(max_points)} points</strong>, tandis que "
        f"<strong>{lowest_teams}</strong> représente le minimum avec "
        f"<strong>{int(min_points)} points</strong>. Les équipes intermédiaires "
        "sont volontairement atténuées pour accélérer la lecture.",
        THEME["green"],
    )

# =============================================================================
# 8. Pied de page
# =============================================================================
st.markdown(
    f"""
    <div style="display:flex;justify-content:space-between;gap:1rem;margin-top:1.1rem;
                padding-top:1rem;border-top:1px solid {THEME['border']};color:{THEME['muted']};
                font-size:.66rem">
      <span>Premier League Performance Review · 2019–2024</span>
      <span>Source : football-data.co.uk · Division E0</span>
    </div>
    """,
    unsafe_allow_html=True,
)
