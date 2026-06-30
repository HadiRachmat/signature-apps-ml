import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Dashboard",
    page_icon="📖",
    layout="wide"
)

st.title("📖 Monitoring Hafalan Al-Qur'an")
st.write("Selamat datang, **Ustadz Ahmad**")

st.divider()

# =========================
# CARD STATISTIK
# =========================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Santri",
    120
)

col2.metric(
    "Hafal 30 Juz",
    35
)

col3.metric(
    "Sedang Aktif",
    85
)

col4.metric(
    "Rata-rata Nilai",
    "88"
)

st.divider()

# =========================
# GRAFIK
# =========================

left, right = st.columns(2)

with left:

    st.subheader("Perkembangan Hafalan")

    data = pd.DataFrame({
        "Minggu":[1,2,3,4,5],
        "Juz":[2,4,6,8,10]
    })

    st.line_chart(
        data.set_index("Minggu")
    )

with right:

    st.subheader("Distribusi Hafalan")

    juz = pd.DataFrame({
        "Juz":[
            "1-5",
            "6-10",
            "11-15",
            "16-20",
            "21-25",
            "26-30"
        ],
        "Santri":[
            20,
            35,
            28,
            18,
            12,
            7
        ]
    })

    st.bar_chart(
        juz.set_index("Juz")
    )

st.divider()

# =========================
# TABEL
# =========================

st.subheader("Data Santri Terbaru")

df = pd.DataFrame({

    "Nama":[
        "Ahmad",
        "Ali",
        "Fatimah",
        "Aisyah",
        "Budi"
    ],

    "Juz":[
        12,
        8,
        15,
        20,
        5
    ],

    "Nilai Tajwid":[
        90,
        88,
        95,
        97,
        82
    ],

    "Kelancaran":[
        87,
        84,
        92,
        95,
        80
    ],

    "Status":[
        "Aktif",
        "Aktif",
        "Aktif",
        "Aktif",
        "Belum Aktif"
    ]

})

st.dataframe(
    df,
    use_container_width=True
)