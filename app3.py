import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="智能护理助手",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    .stApp {
        background: #eef0f3;
    }

    .main .block-container {
        max-width: 100%;
        padding-top: 8px;
        padding-bottom: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

phone_html = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<style>
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    body {
        background: #eef0f3;
        font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
        display: flex;
        justify-content: center;
        align-items: flex-start;
        padding: 24px 0;
    }

    .phone-stage {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        width: 100%;
    }

    .phone-shell {
        width: 390px;
        height: 780px;
        background: linear-gradient(180deg, #1c2230 0%, #0d1320 100%);
        border-radius: 42px;
        padding: 12px;
        box-shadow:
            0 20px 60px rgba(0,0,0,0.20),
            inset 0 0 0 1px rgba(255,255,255,0.10);
        position: relative;
    }

    .phone-frame {
        width: 100%;
        height: 100%;
        border-radius: 34px;
        background: #0f1523;
        padding: 10px;
        box-shadow:
            inset 0 0 0 2px rgba(255,255,255,0.05),
            inset 0 0 20px rgba(255,255,255,0.02);
    }

    .phone-screen {
        width: 100%;
        height: 100%;
        border-radius: 28px;
        background: #f3f4f6;
        position: relative;
        overflow: hidden;
    }

    .status-bar {
        height: 44px;
        padding: 14px 16px 0 16px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        color: #111;
        font-size: 14px;
        font-weight: 700;
        position: relative;
        z-index: 5;
    }

    .status-left {
        padding-left: 8px;
    }

    .status-right {
        display: flex;
        gap: 6px;
        align-items: center;
        font-size: 12px;
        padding-right: 6px;
    }

    .top-bar {
        padding: 8px 18px 10px 18px;
        text-align: center;
        position: relative;
        z-index: 5;
        background: #f3f4f6;
    }

    .top-title {
        font-size: 22px;
        font-weight: 800;
        color: #123a6b;
        line-height: 1.2;
    }

    .top-subtitle {
        margin-top: 6px;
        font-size: 12px;
        color: #93a0b2;
        font-weight: 500;
    }

    .main-view {
        position: absolute;
        top: 92px;
        left: 0;
        right: 0;
        bottom: 0;
    }

    .chat-area {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 88px;
        overflow-y: auto;
        padding: 4px 14px 12px 14px;
        scroll-behavior: smooth;
    }

    .chat-area::-webkit-scrollbar,
    .recording-scroll::-webkit-scrollbar {
        width: 0;
        height: 0;
    }

    .empty-state {
        min-height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 20px 14px 40px 14px;
    }

    .empty-card {
        text-align: center;
        color: #7f90a5;
        max-width: 280px;
    }

    .empty-icon-wrap {
        display: flex;
        justify-content: center;
        margin-bottom: 18px;
    }

    .empty-icon-box {
        width: 74px;
        height: 74px;
        border-radius: 22px;
        background: #eef3f9;
        border: 1px solid #dbe5f1;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 30px;
        color: #7d8795;
    }

    .empty-title {
        font-size: 28px;
        font-weight: 800;
        color: #123a6b;
        margin-bottom: 14px;
        letter-spacing: 1px;
    }

    .empty-desc {
        font-size: 14px;
        line-height: 1.9;
        color: #7f90a5;
        font-weight: 500;
    }

    .message-list {
        display: flex;
        flex-direction: column;
        gap: 10px;
        padding-bottom: 18px;
    }

    .message-row {
        display: flex;
        width: 100%;
    }

    .message-row.user {
        justify-content: flex-end;
    }

    .message-row.assistant {
        justify-content: flex-start;
    }

    .bubble {
        max-width: 78%;
        padding: 11px 14px;
        border-radius: 18px;
        font-size: 14px;
        line-height: 1.7;
        word-break: break-word;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }

    .bubble.user {
        background: #cfe6ff;
        color: #123a6b;
        border-bottom-right-radius: 6px;
    }

    .bubble.assistant {
        background: #ffffff;
        color: #2c3a4d;
        border-bottom-left-radius: 6px;
    }

    .card-wrap {
        max-width: 88%;
    }

    .info-card {
        background: #ffffff;
        border-radius: 18px;
        padding: 14px;
        box-shadow: 0 2px 10px rgba(24,39,75,0.06);
        border: 1px solid #edf1f6;
    }

    .card-title {
        font-size: 15px;
        font-weight: 800;
        color: #123a6b;
        margin-bottom: 10px;
    }

    .card-title-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 10px;
    }

    .card-title-row .card-title {
        margin-bottom: 0;
    }

    .edit-btn {
        height: 30px;
        padding: 0 12px;
        border-radius: 999px;
        border: 1px solid #d7e2ee;
        background: #f8fbff;
        color: #5b7089;
        font-size: 12px;
        font-weight: 700;
        cursor: pointer;
        flex-shrink: 0;
    }

    .inline-action-wrap {
        padding: 0 2px;
    }

    .inline-action-btn {
        width: 100%;
        height: 46px;
        border: none;
        border-radius: 16px;
        background: #123a6b;
        color: #ffffff;
        font-size: 14px;
        font-weight: 800;
        cursor: pointer;
        box-shadow: 0 10px 24px rgba(18,58,107,0.16);
        transition: transform 0.18s ease, opacity 0.18s ease;
    }

    .inline-action-btn:active {
        transform: scale(0.98);
    }

    .inline-action-btn:disabled {
        opacity: 0.55;
        cursor: default;
        transform: none;
    }

    .card-desc {
        font-size: 13px;
        color: #6f8098;
        line-height: 1.7;
        margin-bottom: 10px;
    }

    .tag-row {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 8px;
    }

    .tag {
        display: inline-flex;
        align-items: center;
        padding: 5px 10px;
        border-radius: 999px;
        background: #f3f7fc;
        color: #4b6688;
        font-size: 12px;
        font-weight: 700;
    }

    .tag-warning {
        background: #fff1ee;
        color: #c34a39;
    }

    .tag-positive {
        background: #ebf8f0;
        color: #2f7b48;
    }

    .tag-watch {
        background: #fff8e8;
        color: #956d1f;
    }

    table.data-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 4px;
        overflow: hidden;
        border-radius: 12px;
    }

    table.data-table th {
        background: #f6f8fb;
        color: #60758f;
        font-size: 12px;
        font-weight: 700;
        text-align: left;
        padding: 9px 8px;
        border-bottom: 1px solid #ebf0f5;
    }

    table.data-table td {
        padding: 10px 8px;
        font-size: 12px;
        color: #2f3e52;
        border-bottom: 1px solid #eef2f7;
        vertical-align: top;
    }

    table.data-table tr:last-child td {
        border-bottom: none;
    }

    .list-card {
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-top: 4px;
    }

    .list-item {
        padding: 10px 12px;
        background: #f8fafc;
        border-radius: 12px;
        border: 1px solid #edf1f6;
    }

    .list-main {
        font-size: 13px;
        font-weight: 700;
        color: #24384f;
        margin-bottom: 4px;
    }

    .list-sub {
        font-size: 12px;
        line-height: 1.6;
        color: #71839a;
    }

    .profile-grid {
        display: grid;
        grid-template-columns: 76px 1fr;
        row-gap: 8px;
        column-gap: 8px;
        margin-top: 4px;
    }

    .profile-label {
        font-size: 12px;
        color: #7a8ca4;
        font-weight: 700;
    }

    .profile-value {
        font-size: 12px;
        color: #2e3d52;
        line-height: 1.7;
    }

    .bottom-panel {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        padding: 10px 12px 18px 12px;
        background: linear-gradient(180deg, rgba(243,244,246,0.00) 0%, rgba(243,244,246,0.72) 10%, #f3f4f6 22%, #f3f4f6 100%);
    }

    .chips-scroll {
        overflow-x: auto;
        white-space: nowrap;
        padding: 0 2px 8px 2px;
        scrollbar-width: none;
    }

    .chips-scroll::-webkit-scrollbar {
        display: none;
    }

    .chip-btn {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: #ffffff;
        color: #123a6b;
        border: 1px solid #e6ebf2;
        border-radius: 999px;
        padding: 10px 14px;
        margin-right: 8px;
        font-size: 14px;
        font-weight: 700;
        box-shadow: 0 2px 8px rgba(18,58,107,0.04);
        cursor: pointer;
        user-select: none;
        transition: all 0.18s ease;
    }

    .chip-btn:active {
        transform: scale(0.98);
        background: #f5f7fa;
    }

    .chip-btn.primary {
        background: linear-gradient(135deg, #123a6b 0%, #265a92 100%);
        color: #ffffff;
        border-color: transparent;
    }

    .input-row {
        display: flex;
        align-items: center;
        gap: 10px;
        background: #ffffff;
        border: 1px solid #e8edf3;
        border-radius: 24px;
        padding: 7px 8px 7px 14px;
        box-shadow: 0 2px 12px rgba(24,39,75,0.05);
    }

    .text-input {
        flex: 1;
        border: none;
        outline: none;
        background: transparent;
        color: #34465b;
        font-size: 14px;
        line-height: 1;
        min-width: 0;
    }

    .text-input::placeholder {
        color: #a1adbc;
    }

    .input-actions {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-shrink: 0;
    }

    .input-action-btn {
        width: 34px;
        height: 34px;
        border-radius: 50%;
        border: none;
        background: #ffffff;
        cursor: pointer;
        box-shadow: inset 0 0 0 1px #dde6f0;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        transition: transform 0.18s ease, background 0.18s ease;
    }

    .input-action-btn:active {
        transform: scale(0.96);
        background: #f5f7fa;
    }

    .input-action-btn svg {
        width: 17px;
        height: 17px;
        stroke: #1f2f43;
        stroke-width: 2;
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .more-btn svg {
        width: 18px;
        height: 18px;
    }

    .history-view {
        position: absolute;
        top: 92px;
        left: 0;
        right: 0;
        bottom: 0;
        background: #f3f4f6;
    }

    .history-scroll {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 84px;
        overflow-y: auto;
        padding: 12px 14px 18px 14px;
        scrollbar-width: none;
    }

    .history-scroll::-webkit-scrollbar {
        width: 0;
        height: 0;
    }

    .archive-list {
        display: flex;
        flex-direction: column;
        gap: 12px;
    }

    .archive-card {
        width: 100%;
        border: none;
        background: #ffffff;
        border-radius: 18px;
        padding: 14px;
        text-align: left;
        box-shadow: 0 2px 10px rgba(24,39,75,0.06);
        border: 1px solid #edf1f6;
        cursor: pointer;
        transition: transform 0.18s ease, box-shadow 0.18s ease;
    }

    .archive-card:active {
        transform: scale(0.99);
        box-shadow: 0 1px 6px rgba(24,39,75,0.08);
    }

    .archive-card-top {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        align-items: flex-start;
    }

    .archive-card-main {
        flex: 1;
        min-width: 0;
    }

    .archive-name {
        font-size: 16px;
        font-weight: 800;
        color: #123a6b;
    }

    .archive-service {
        margin-top: 4px;
        font-size: 13px;
        color: #687c95;
        line-height: 1.6;
    }

    .archive-time {
        font-size: 11px;
        color: #90a0b4;
        font-weight: 700;
        text-align: right;
        line-height: 1.5;
        flex-shrink: 0;
    }

    .archive-status-row {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-top: 12px;
        flex-wrap: wrap;
    }

    .archive-status-pill {
        display: inline-flex;
        align-items: center;
        padding: 6px 10px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 800;
    }

    .archive-status-pill.warning {
        background: #fff1ee;
        color: #c34a39;
    }

    .archive-status-pill.positive {
        background: #ebf8f0;
        color: #2f7b48;
    }

    .archive-status-pill.watch {
        background: #fff8e8;
        color: #956d1f;
    }

    .archive-scene {
        font-size: 12px;
        color: #7d8ea4;
        font-weight: 700;
    }

    .archive-summary {
        margin-top: 10px;
        font-size: 13px;
        color: #2f3e52;
        line-height: 1.75;
    }

    .archive-meta-note {
        margin-top: 10px;
        font-size: 12px;
        color: #8a9ab0;
        line-height: 1.7;
    }

    .sheet-overlay {
        position: absolute;
        inset: 0;
        background: rgba(12, 20, 32, 0.22);
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.22s ease;
        z-index: 14;
    }

    .sheet-overlay.visible {
        opacity: 1;
        pointer-events: auto;
    }

    .more-sheet {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        background: #ffffff;
        border-radius: 28px 28px 0 0;
        padding: 10px 14px 24px 14px;
        box-shadow: 0 -18px 36px rgba(16, 35, 59, 0.12);
        transform: translateY(100%);
        transition: transform 0.24s ease;
        z-index: 15;
        pointer-events: none;
    }

    .more-sheet.visible {
        transform: translateY(0);
        pointer-events: auto;
    }

    .sheet-handle {
        width: 42px;
        height: 5px;
        border-radius: 999px;
        background: #d7e0ea;
        margin: 2px auto 14px auto;
    }

    .sheet-title {
        font-size: 18px;
        font-weight: 800;
        color: #123a6b;
        text-align: center;
    }

    .sheet-subtitle {
        margin-top: 6px;
        font-size: 12px;
        color: #8b9bb0;
        text-align: center;
        line-height: 1.7;
    }

    .sheet-grid {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-top: 18px;
    }

    .sheet-action-card {
        border: none;
        background: transparent;
        padding: 0;
        cursor: pointer;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
        width: 100%;
    }

    .sheet-icon-box {
        width: 58px;
        height: 58px;
        margin: 0 auto;
        border-radius: 18px;
        background: #f4f7fb;
        border: 1px solid #e6edf4;
        display: flex;
        align-items: center;
        justify-content: center;
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.7);
    }

    .sheet-icon-box svg {
        width: 24px;
        height: 24px;
        stroke: #123a6b;
        stroke-width: 2;
        fill: none;
        stroke-linecap: round;
        stroke-linejoin: round;
    }

    .sheet-action-label {
        display: flex;
        align-items: flex-start;
        justify-content: center;
        margin-top: 9px;
        font-size: 12px;
        color: #50657f;
        font-weight: 700;
        line-height: 1.5;
        min-height: 36px;
        width: 100%;
        text-align: center;
    }

    .sheet-helper {
        margin-top: 16px;
        font-size: 12px;
        color: #97a6b8;
        line-height: 1.7;
        text-align: center;
    }

    .recording-view {
        position: absolute;
        top: 92px;
        left: 0;
        right: 0;
        bottom: 0;
        background: #f3f4f6;
    }

    .recording-scroll {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 92px;
        overflow-y: auto;
        padding: 12px 14px 18px 14px;
        scrollbar-width: none;
    }

    .recording-hero {
        padding: 2px 2px 14px 2px;
    }

    .scene-badge {
        display: inline-flex;
        align-items: center;
        padding: 6px 10px;
        border-radius: 999px;
        background: #ebf1f8;
        color: #4a6284;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .recording-hero-title {
        font-size: 28px;
        font-weight: 800;
        color: #123a6b;
        line-height: 1.2;
    }

    .recording-hero-desc {
        margin-top: 8px;
        color: #7f90a5;
        font-size: 13px;
        line-height: 1.8;
    }

    .recording-stack {
        display: flex;
        flex-direction: column;
        gap: 12px;
        padding-bottom: 10px;
    }

    .live-audio-card {
        overflow: hidden;
    }

    .live-audio-row,
    .playback-audio-row {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .audio-main {
        flex: 1;
        min-width: 0;
    }

    .audio-main-title {
        font-size: 15px;
        font-weight: 800;
        color: #123a6b;
        line-height: 1.4;
    }

    .audio-main-desc {
        margin-top: 4px;
        font-size: 12px;
        color: #7f90a5;
        line-height: 1.7;
    }

    .audio-wave-shell {
        margin-top: 12px;
        background: #f7f9fc;
        border: 1px solid #e8eef5;
        border-radius: 16px;
        padding: 12px 14px;
        overflow: hidden;
    }

    .audio-wave-top {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 12px;
        margin-bottom: 8px;
    }

    .audio-wave-label {
        font-size: 12px;
        font-weight: 700;
        color: #627893;
    }

    .audio-wave-time {
        font-size: 12px;
        font-weight: 800;
        color: #123a6b;
    }

    .audio-wave-track {
        position: relative;
        height: 42px;
        display: flex;
        align-items: center;
    }

    .audio-wave-bg {
        position: absolute;
        inset: 0;
        border-radius: 12px;
        background: linear-gradient(90deg, rgba(18,58,107,0.04) 0%, rgba(18,58,107,0.10) 100%);
    }

    .audio-wave-progress {
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        width: 36%;
        border-radius: 12px;
        background: linear-gradient(90deg, rgba(18,58,107,0.12) 0%, rgba(38,90,146,0.18) 100%);
        opacity: 0;
    }

    .wave-bars {
        position: relative;
        z-index: 1;
        width: 100%;
        height: 100%;
        display: flex;
        align-items: center;
        gap: 3px;
    }

    .wave-bar {
        flex: 1;
        min-width: 3px;
        border-radius: 999px;
        background: #9bb0c8;
        height: 28%;
    }

    .wave-bars.live .wave-bar {
        animation: wavePulse 1.4s ease-in-out infinite;
        background: linear-gradient(180deg, #77a2d1 0%, #123a6b 100%);
    }

    .wave-bars.live.stopped {
        display: none;
    }

    .wave-bars.playback .wave-bar {
        background: linear-gradient(180deg, #c8d6e6 0%, #8ea7c3 100%);
        opacity: 0;
    }

    .wave-bars.playback .wave-bar.active {
        background: linear-gradient(180deg, #77a2d1 0%, #123a6b 100%);
    }

    .playback-audio-card.is-playing .audio-wave-progress {
        opacity: 1;
        animation: playbackSweep 2.4s linear infinite;
    }

    .playback-audio-card.is-playing .wave-bars.playback .wave-bar {
        opacity: 1;
        animation: wavePulse 1.4s ease-in-out infinite;
    }

    @keyframes playbackSweep {
        0% {
            width: 12%;
            opacity: 0.55;
        }
        50% {
            width: 56%;
            opacity: 0.95;
        }
        100% {
            width: 90%;
            opacity: 0.55;
        }
    }

    @keyframes wavePulse {
        0%, 100% {
            height: 24%;
        }
        20% {
            height: 78%;
        }
        45% {
            height: 42%;
        }
        70% {
            height: 66%;
        }
    }

    .stream-card {
        min-height: 250px;
    }

    .streaming-list {
        min-height: 170px;
    }

    .stream-line {
        animation: streamFadeIn 0.28s ease;
    }

    @keyframes streamFadeIn {
        from {
            opacity: 0;
            transform: translateY(6px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .stream-placeholder {
        min-height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 18px 14px;
        border-radius: 14px;
        background: #f8fafc;
        border: 1px solid #edf1f6;
        color: #95a3b5;
        font-size: 13px;
        line-height: 1.8;
        text-align: center;
    }

    .playback-audio-card {
        padding-bottom: 16px;
    }

    .play-btn {
        width: 42px;
        height: 42px;
        flex-shrink: 0;
        border-radius: 50%;
        border: none;
        background: #123a6b;
        color: #ffffff;
        font-size: 16px;
        font-weight: 800;
        box-shadow: 0 10px 24px rgba(18,58,107,0.16);
        cursor: pointer;
    }

    .play-btn:active {
        transform: scale(0.97);
    }

    .status-card-top {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        gap: 12px;
    }

    .status-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 12px;
        border-radius: 999px;
        background: #fff1ee;
        color: #c34a39;
        font-size: 12px;
        font-weight: 800;
        flex-shrink: 0;
    }

    .status-pill.stopped {
        background: #eef3f8;
        color: #5f7086;
    }

    .record-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #ff5a46;
        box-shadow: 0 0 0 0 rgba(255, 90, 70, 0.56);
        animation: recordPulse 1.4s infinite;
    }

    .status-pill.stopped .record-dot {
        background: #9aa8b9;
        box-shadow: none;
        animation: none;
    }

    @keyframes recordPulse {
        0% {
            box-shadow: 0 0 0 0 rgba(255, 90, 70, 0.56);
        }
        70% {
            box-shadow: 0 0 0 10px rgba(255, 90, 70, 0);
        }
        100% {
            box-shadow: 0 0 0 0 rgba(255, 90, 70, 0);
        }
    }

    .service-grid {
        display: grid;
        grid-template-columns: 82px 1fr;
        row-gap: 9px;
        column-gap: 8px;
        margin-top: 14px;
    }

    .service-label {
        font-size: 12px;
        color: #7a8ca4;
        font-weight: 700;
    }

    .service-value {
        font-size: 13px;
        color: #2e3d52;
        line-height: 1.7;
        font-weight: 600;
    }

    .recording-note {
        margin-top: 14px;
        padding: 12px;
        border-radius: 14px;
        background: #f7f9fc;
        border: 1px solid #edf1f6;
        color: #6f8098;
        font-size: 13px;
        line-height: 1.7;
    }

    .helper-text {
        color: #8c99aa;
        font-size: 12px;
        line-height: 1.7;
        margin-top: 8px;
    }

    .loading-card {
        display: flex;
        align-items: center;
        gap: 12px;
    }

    .loading-spinner {
        width: 24px;
        height: 24px;
        border: 3px solid #dce6f3;
        border-top-color: #123a6b;
        border-radius: 50%;
        animation: spin 0.9s linear infinite;
        flex-shrink: 0;
    }

    @keyframes spin {
        to {
            transform: rotate(360deg);
        }
    }

    .transcript-list {
        display: flex;
        flex-direction: column;
        gap: 10px;
    }

    .transcript-line {
        padding: 11px 12px;
        background: #f8fafc;
        border-radius: 14px;
        border: 1px solid #edf1f6;
    }

    .transcript-speaker {
        display: block;
        font-size: 12px;
        font-weight: 800;
        color: #123a6b;
        margin-bottom: 4px;
    }

    .transcript-text {
        font-size: 13px;
        line-height: 1.7;
        color: #34465b;
    }

    .analysis-summary {
        margin-top: 6px;
        padding: 12px;
        border-radius: 14px;
        font-size: 13px;
        font-weight: 800;
        line-height: 1.6;
    }

    .tone-warning {
        background: #fff1ee;
        color: #c34a39;
    }

    .tone-positive {
        background: #ecf8f0;
        color: #2f7b48;
    }

    .tone-watch {
        background: #fff7e6;
        color: #9a7217;
    }

    .analysis-grid {
        display: grid;
        grid-template-columns: 86px 1fr;
        row-gap: 10px;
        column-gap: 8px;
        margin-top: 14px;
    }

    .analysis-label {
        font-size: 12px;
        color: #7a8ca4;
        font-weight: 700;
    }

    .analysis-value {
        font-size: 13px;
        color: #2f3e52;
        line-height: 1.75;
    }

    .recording-footer {
        position: absolute;
        left: 0;
        right: 0;
        bottom: 0;
        display: flex;
        gap: 10px;
        padding: 12px 14px 18px 14px;
        background: linear-gradient(180deg, rgba(243,244,246,0.00) 0%, rgba(243,244,246,0.72) 12%, #f3f4f6 28%, #f3f4f6 100%);
    }

    .footer-btn {
        height: 48px;
        border-radius: 18px;
        border: none;
        font-size: 14px;
        font-weight: 800;
        cursor: pointer;
        transition: transform 0.18s ease, opacity 0.18s ease;
    }

    .footer-btn.primary {
        flex: 1.2;
        background: #123a6b;
        color: #ffffff;
        box-shadow: 0 10px 24px rgba(18,58,107,0.16);
    }

    .footer-btn.secondary {
        flex: 0.9;
        background: #ffffff;
        color: #46596f;
        border: 1px solid #e2e9f1;
        box-shadow: 0 4px 14px rgba(24,39,75,0.05);
    }

    .footer-btn:active {
        transform: scale(0.98);
    }

    .footer-btn:disabled {
        opacity: 0.55;
        cursor: default;
        transform: none;
    }

    .home-indicator {
        position: absolute;
        bottom: 6px;
        left: 50%;
        transform: translateX(-50%);
        width: 134px;
        height: 5px;
        border-radius: 999px;
        background: rgba(0,0,0,0.28);
    }

    .hidden {
        display: none !important;
    }
</style>
</head>
<body>
    <div class="phone-stage">
        <div class="phone-shell">
            <div class="phone-frame">
                <div class="phone-screen">
                    <div class="status-bar">
                        <div class="status-left">9:41</div>
                        <div class="status-right">
                            <span>📶</span>
                            <span>📡</span>
                            <span>🔋</span>
                        </div>
                    </div>

                    <div class="top-bar">
                        <div id="topTitle" class="top-title">AI护理助手</div>
                        <div id="topSubtitle" class="top-subtitle">护理助手与服务留痕</div>
                    </div>

                    <div id="mainView" class="main-view">
                        <div id="chatArea" class="chat-area">
                            <div id="emptyState" class="empty-state"></div>
                            <div id="messageList" class="message-list"></div>
                        </div>

                        <div class="bottom-panel">
                            <div class="input-row">
                                <input id="textInput" class="text-input" placeholder="发送消息或按回车发送..." />
                                <div class="input-actions">
                                    <button id="voiceBtn" class="input-action-btn" title="语音输入" type="button" aria-label="语音输入">
                                        <svg viewBox="0 0 24 24" aria-hidden="true">
                                            <path d="M12 5.5a2.8 2.8 0 0 1 2.8 2.8v4.2a2.8 2.8 0 1 1-5.6 0V8.3A2.8 2.8 0 0 1 12 5.5Z"></path>
                                            <path d="M7.8 12.5a4.2 4.2 0 0 0 8.4 0"></path>
                                            <path d="M12 16.7V19"></path>
                                        </svg>
                                    </button>
                                    <button id="moreBtn" class="input-action-btn more-btn" title="更多功能" type="button" aria-label="更多功能">
                                        <svg viewBox="0 0 24 24" aria-hidden="true">
                                            <path d="M12 5v14"></path>
                                            <path d="M5 12h14"></path>
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div id="recordingView" class="recording-view hidden">
                        <div class="recording-scroll">
                            <div id="recordingContent" class="recording-stack"></div>
                        </div>

                        <div class="recording-footer">
                            <button id="analyzeBtn" class="footer-btn primary" style="flex:1;">生成AI分析</button>
                        </div>
                    </div>

                    <div id="historyListView" class="history-view hidden">
                        <div id="historyListContent" class="history-scroll"></div>
                        <div class="recording-footer">
                            <button id="historyListBackBtn" class="footer-btn secondary" style="flex:1;">返回助手</button>
                        </div>
                    </div>

                    <div id="historyDetailView" class="history-view hidden">
                        <div id="historyDetailContent" class="history-scroll"></div>
                        <div class="recording-footer">
                            <button id="historyDetailBackBtn" class="footer-btn secondary">返回列表</button>
                            <button id="historyDetailHomeBtn" class="footer-btn primary">返回助手</button>
                        </div>
                    </div>

                    <div id="sheetOverlay" class="sheet-overlay"></div>
                    <div id="moreSheet" class="more-sheet">
                        <div class="sheet-handle"></div>
                        <div class="sheet-title">更多功能</div>
                        <div class="sheet-subtitle">点击下方入口可发起 AI 智能服务或查看历史服务归档，后续能力将在此处继续扩展。</div>
                        <div class="sheet-grid">
                            <button id="fullRecordMenuBtn" class="sheet-action-card" type="button">
                                <div class="sheet-icon-box">
                                    <svg viewBox="0 0 24 24" aria-hidden="true">
                                        <circle cx="12" cy="12" r="7"></circle>
                                        <circle cx="12" cy="12" r="2.5" fill="#123a6b" stroke="none"></circle>
                                    </svg>
                                </div>
                                <span class="sheet-action-label">AI智能服务</span>
                            </button>
                            <button id="historyMenuBtn" class="sheet-action-card" type="button">
                                <div class="sheet-icon-box">
                                    <svg viewBox="0 0 24 24" aria-hidden="true">
                                        <rect x="4.5" y="4.5" width="15" height="15" rx="3"></rect>
                                        <path d="M8 9h8"></path>
                                        <path d="M8 12.5h8"></path>
                                        <path d="M8 16h5"></path>
                                    </svg>
                                </div>
                                <span class="sheet-action-label">历史服务记录</span>
                            </button>
                        </div>
                        <div class="sheet-helper">当前菜单已开放“AI智能服务”和“历史服务记录”，其余扩展能力将在后续版本中接入。</div>
                    </div>

                    <div class="home-indicator"></div>
                </div>
            </div>
        </div>
    </div>

<script>
    const DEFAULT_TOP = {
        title: "AI护理助手",
        subtitle: "护理助手与服务留痕"
    };

    const RECORDING_TOP = {
        title: "AI智能服务",
        subtitle: "服务录音转写与智能分析"
    };

    const ANALYSIS_TOP = {
        title: "AI智能分析",
        subtitle: "服务录音、对话内容与智能建议"
    };

    const HISTORY_LIST_TOP = {
        title: "历史服务记录",
        subtitle: "查看全程录音分析后的服务归档"
    };

    const HISTORY_DETAIL_TOP = {
        title: "服务记录详情",
        subtitle: "查看录音分析后的完整归档记录"
    };

    const topTitle = document.getElementById("topTitle");
    const topSubtitle = document.getElementById("topSubtitle");
    const mainView = document.getElementById("mainView");
    const recordingView = document.getElementById("recordingView");
    const historyListView = document.getElementById("historyListView");
    const historyDetailView = document.getElementById("historyDetailView");
    const recordingContent = document.getElementById("recordingContent");
    const historyListContent = document.getElementById("historyListContent");
    const historyDetailContent = document.getElementById("historyDetailContent");
    const analyzeBtn = document.getElementById("analyzeBtn");
    const historyListBackBtn = document.getElementById("historyListBackBtn");
    const historyDetailBackBtn = document.getElementById("historyDetailBackBtn");
    const historyDetailHomeBtn = document.getElementById("historyDetailHomeBtn");
    const messageList = document.getElementById("messageList");
    const emptyState = document.getElementById("emptyState");
    const chatArea = document.getElementById("chatArea");
    const textInput = document.getElementById("textInput");
    const voiceBtn = document.getElementById("voiceBtn");
    const moreBtn = document.getElementById("moreBtn");
    const sheetOverlay = document.getElementById("sheetOverlay");
    const moreSheet = document.getElementById("moreSheet");
    const fullRecordMenuBtn = document.getElementById("fullRecordMenuBtn");
    const historyMenuBtn = document.getElementById("historyMenuBtn");
    const chipButtons = document.querySelectorAll(".chip-btn");

    let voiceIndex = 0;
    let recordingScenarioIndex = 0;
    let currentRecordingScenario = null;
    let recordingAnalyzed = false;
    let analyzingTimer = null;
    let transcriptStreamTimer = null;
    let streamedTranscriptCount = 0;
    let transcriptStarted = false;
    let transcriptCompleted = false;
    let historyRecordCounter = 0;
    let historyRecords = [];
    let currentHistoryRecord = null;

    const presetData = {
        task: {
            user: "我要查看今日护理任务",
            assistant: "已为您查询到今日护理任务，今天共有 4 项护理安排，请按时完成并做好记录。",
            card: `
                <div class="info-card">
                    <div class="card-title">今日护理任务</div>
                    <div class="card-desc">日期：2026-04-22｜班次：白班｜执行护理员：李护理员</div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>老人</th>
                                <th>床位</th>
                                <th>任务</th>
                                <th>时间</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>王秀兰</td>
                                <td>A-201</td>
                                <td>晨间测压、服药提醒</td>
                                <td>08:30</td>
                            </tr>
                            <tr>
                                <td>张建国</td>
                                <td>A-203</td>
                                <td>血糖检测、早餐协助</td>
                                <td>09:00</td>
                            </tr>
                            <tr>
                                <td>李阿婆</td>
                                <td>B-105</td>
                                <td>翻身护理、皮肤观察</td>
                                <td>10:00</td>
                            </tr>
                            <tr>
                                <td>赵明德</td>
                                <td>B-108</td>
                                <td>康复训练陪护</td>
                                <td>14:30</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            `
        },
        bed: {
            user: "查看床位清单",
            assistant: "已为您展示当前床位占用情况，以下为当前床位数据。",
            card: `
                <div class="info-card">
                    <div class="card-title">床位清单</div>
                    <div class="card-desc">当前楼层：2F、3F｜总床位：8｜已入住：6｜空床：2</div>
                    <table class="data-table">
                        <thead>
                            <tr>
                                <th>床位</th>
                                <th>状态</th>
                                <th>入住老人</th>
                                <th>备注</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td>A-201</td>
                                <td>已入住</td>
                                <td>王秀兰</td>
                                <td>高血压</td>
                            </tr>
                            <tr>
                                <td>A-202</td>
                                <td>空床</td>
                                <td>-</td>
                                <td>待整理</td>
                            </tr>
                            <tr>
                                <td>A-203</td>
                                <td>已入住</td>
                                <td>张建国</td>
                                <td>糖尿病</td>
                            </tr>
                            <tr>
                                <td>B-105</td>
                                <td>已入住</td>
                                <td>李阿婆</td>
                                <td>卧床观察</td>
                            </tr>
                            <tr>
                                <td>B-108</td>
                                <td>已入住</td>
                                <td>赵明德</td>
                                <td>康复中</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            `
        },
        todo: {
            user: "查询待办服务",
            assistant: "已为您整理当前待办服务，建议优先处理临近超时任务。",
            card: `
                <div class="info-card">
                    <div class="card-title">待办服务</div>
                    <div class="list-card">
                        <div class="list-item">
                            <div class="list-main">王秀兰｜12:00 服药复核</div>
                            <div class="list-sub">需确认午间降压药是否已按医嘱服用，并记录血压值。</div>
                        </div>
                        <div class="list-item">
                            <div class="list-main">张建国｜14:00 血糖复测</div>
                            <div class="list-sub">餐后两小时复测血糖，注意记录异常波动。</div>
                        </div>
                        <div class="list-item">
                            <div class="list-main">李阿婆｜15:00 翻身护理</div>
                            <div class="list-sub">卧床老人需定时翻身，观察受压部位皮肤情况。</div>
                        </div>
                    </div>
                </div>
            `
        },
        focus: {
            user: "查询重点关注对象",
            assistant: "以下为当前重点关注对象及护理提醒，请加强巡查频率。",
            card: `
                <div class="info-card">
                    <div class="card-title">重点关注对象</div>
                    <div class="list-card">
                        <div class="list-item">
                            <div class="list-main">王秀兰｜A-201</div>
                            <div class="list-sub">高血压波动，需关注晨晚血压；服药后 30 分钟复测。</div>
                        </div>
                        <div class="list-item">
                            <div class="list-main">李阿婆｜B-105</div>
                            <div class="list-sub">长期卧床，需关注压疮风险与皮肤完整性。</div>
                        </div>
                        <div class="list-item">
                            <div class="list-main">赵明德｜B-108</div>
                            <div class="list-sub">康复训练期，步态不稳，转移时需双人辅助。</div>
                        </div>
                    </div>
                    <div class="tag-row">
                        <span class="tag">高血压</span>
                        <span class="tag">卧床风险</span>
                        <span class="tag">跌倒预警</span>
                    </div>
                </div>
            `
        },
        profile: {
            user: "查询王秀兰老人基本情况",
            assistant: "已为您调取王秀兰老人的基础信息与照护重点。",
            card: `
                <div class="info-card">
                    <div class="card-title">王秀兰老人基本情况</div>
                    <div class="profile-grid">
                        <div class="profile-label">姓名</div><div class="profile-value">王秀兰</div>
                        <div class="profile-label">年龄</div><div class="profile-value">82 岁</div>
                        <div class="profile-label">床位</div><div class="profile-value">A-201</div>
                        <div class="profile-label">护理等级</div><div class="profile-value">二级护理</div>
                        <div class="profile-label">基础病史</div><div class="profile-value">高血压、冠心病</div>
                        <div class="profile-label">当前情况</div><div class="profile-value">精神状态平稳，可自主进食，晨间血压偏高，需继续观察。</div>
                        <div class="profile-label">照护重点</div><div class="profile-value">规律服药、晨晚血压监测、防跌倒提醒。</div>
                    </div>
                </div>
            `
        },
        care_record: {
            user: "我刚刚给王秀兰老人量了血压，喂了降压药，协助洗澡，还做了压疮护理，翻身一次，皮肤没有明显异常，老人整体状态稳定。",
            assistant: "已根据您的语音内容自动整理护理记录，请确认本次服务信息。",
            card: `
                <div class="info-card">
                    <div class="card-title">护理记录表单</div>
                    <div class="card-desc">记录方式：语音自动生成｜记录时间：2026-04-22 10:30</div>
                    <div class="profile-grid">
                        <div class="profile-label">服务对象</div><div class="profile-value">王秀兰</div>
                        <div class="profile-label">床位号</div><div class="profile-value">A-201</div>
                        <div class="profile-label">护理员</div><div class="profile-value">李护理员</div>
                        <div class="profile-label">服务项目</div><div class="profile-value">血压测量、喂药、洗澡协助、压疮护理、翻身护理</div>
                        <div class="profile-label">执行情况</div><div class="profile-value">上述护理项目均已完成。</div>
                        <div class="profile-label">观察结果</div><div class="profile-value">皮肤无明显破损或发红，老人情绪稳定，配合度良好。</div>
                        <div class="profile-label">异常情况</div><div class="profile-value">未见明显异常。</div>
                        <div class="profile-label">后续建议</div><div class="profile-value">继续关注皮肤受压部位，按计划进行翻身护理与生命体征监测。</div>
                    </div>
                    <div class="tag-row">
                        <span class="tag">语音生成</span>
                        <span class="tag">护理留痕</span>
                        <span class="tag">已完成</span>
                    </div>
                </div>
            `
        }
    };

    const recordingScenarios = [
        {
            sceneLabel: "异常服务",
            tone: "warning",
            resident: "王秀兰",
            bed: "A-201",
            service: "翻身护理 / 擦浴协助",
            worker: "李护理员",
            startTime: "2026-04-22 10:12:24",
            endTime: "2026-04-22 10:18:42",
            duration: "06:18",
            banner: "检测到明显负面体验信号",
            summary: "服务过程中，老人多次表达疼痛与明显不适，对护工动作力度和服务节奏表示持续不满。",
            keyFeedback: "老人多次提到“疼”“不舒服”“太急了”。",
            satisfaction: "不满意",
            conclusion: "本次服务存在明显负面体验信号，建议复核。",
            suggestion: "建议班组长复核本次服务过程，并关注后续同类服务动作力度。",
            tags: [
                { text: "老人不满意", tone: "warning" },
                { text: "疼痛反馈", tone: "warning" },
                { text: "服务动作需优化", tone: "watch" },
                { text: "建议复核", tone: "warning" }
            ],
            transcript: [
                { speaker: "护工", text: "王奶奶，我先帮您翻一下身。" },
                { speaker: "老人", text: "你轻一点，刚刚弄得我有点疼。" },
                { speaker: "护工", text: "好，马上就好了。" },
                { speaker: "老人", text: "你别这么用力，还是疼。" },
                { speaker: "老人", text: "你每次都这么急，我很不舒服。" },
                { speaker: "护工", text: "再坚持一下，很快就好了。" },
                { speaker: "老人", text: "我不想你这样弄，太难受了。" }
            ]
        },
        {
            sceneLabel: "满意服务",
            tone: "positive",
            resident: "王秀兰",
            bed: "A-201",
            service: "擦浴协助 / 床铺整理",
            worker: "李护理员",
            startTime: "2026-04-22 09:18:10",
            endTime: "2026-04-22 09:23:52",
            duration: "05:42",
            banner: "本次服务体验良好",
            summary: "服务过程中沟通顺畅，老人情绪平稳，并明确表达认可，整体体验良好。",
            keyFeedback: "老人明确表示“可以，挺舒服的”“谢谢你”。",
            satisfaction: "满意",
            conclusion: "本次服务沟通平稳，服务体验良好。",
            suggestion: "建议保持当前沟通方式与服务节奏，作为正向服务样本留存。",
            tags: [
                { text: "老人满意", tone: "positive" },
                { text: "沟通顺畅", tone: "positive" },
                { text: "服务完成", tone: "positive" }
            ],
            transcript: [
                { speaker: "护工", text: "王奶奶，我现在帮您擦洗一下身体，再给您翻个身，可以吗？" },
                { speaker: "老人", text: "可以，你慢一点就行。" },
                { speaker: "护工", text: "好，现在这样力度可以吗？" },
                { speaker: "老人", text: "可以，挺舒服的。" },
                { speaker: "护工", text: "一会儿我再帮您整理床铺。" },
                { speaker: "老人", text: "好，谢谢你。" },
                { speaker: "护工", text: "不客气，您有不舒服随时告诉我。" }
            ]
        },
        {
            sceneLabel: "轻微不适",
            tone: "watch",
            resident: "王秀兰",
            bed: "A-201",
            service: "翻身护理",
            worker: "李护理员",
            startTime: "2026-04-22 08:41:06",
            endTime: "2026-04-22 08:46:02",
            duration: "04:56",
            banner: "存在轻微不适反馈，已通过沟通缓和",
            summary: "服务过程中老人短暂表达不适，护工及时调整动作与节奏，沟通后情绪恢复平稳。",
            keyFeedback: "老人一次表达“有点酸”，后续反馈缓和。",
            satisfaction: "中性偏负向",
            conclusion: "本次服务存在轻微不适反馈，但已通过沟通调整。",
            suggestion: "建议后续同类服务继续关注动作力度，并保持过程中的确认沟通。",
            tags: [
                { text: "轻微不适反馈", tone: "watch" },
                { text: "沟通安抚有效", tone: "positive" },
                { text: "建议关注动作力度", tone: "watch" }
            ],
            transcript: [
                { speaker: "护工", text: "王奶奶，我帮您翻一下身。" },
                { speaker: "老人", text: "你轻一点，我这边有点酸。" },
                { speaker: "护工", text: "好，我慢一点，现在这样可以吗？" },
                { speaker: "老人", text: "嗯，这样好一点。" },
                { speaker: "护工", text: "现在还疼吗？" },
                { speaker: "老人", text: "还好，没有刚才那么难受了。" }
            ]
        }
    ];

    const initialHistoryEntries = [
        { sceneLabel: "异常服务", archivedAt: "2026-04-22 10:36" },
        { sceneLabel: "满意服务", archivedAt: "2026-04-22 09:48" },
        { sceneLabel: "轻微不适", archivedAt: "2026-04-22 08:55" }
    ];

    const voiceSequence = ["task", "care_record", "profile", "bed", "focus"];

    function setTopBar(content) {
        topTitle.textContent = content.title;
        topSubtitle.textContent = content.subtitle;
    }

    function hideAllViews() {
        [mainView, recordingView, historyListView, historyDetailView].forEach(view => {
            view.classList.add("hidden");
        });
    }

    function showView(targetView, topConfig) {
        closeMoreSheet();
        hideAllViews();
        targetView.classList.remove("hidden");
        setTopBar(topConfig);
    }

    function openMoreSheet() {
        if (moreSheet.classList.contains("visible")) {
            closeMoreSheet();
            return;
        }

        sheetOverlay.classList.add("visible");
        moreSheet.classList.add("visible");
    }

    function closeMoreSheet() {
        sheetOverlay.classList.remove("visible");
        moreSheet.classList.remove("visible");
    }

    function getScenarioByLabel(label) {
        return recordingScenarios.find(item => item.sceneLabel === label);
    }

    function getNextArchiveTimestamp() {
        historyRecordCounter += 1;
        const totalMinutes = (10 * 60 + 36) + historyRecordCounter * 9;
        const hour = String(Math.floor(totalMinutes / 60)).padStart(2, "0");
        const minute = String(totalMinutes % 60).padStart(2, "0");
        return `2026-04-22 ${hour}:${minute}`;
    }

    function createHistoryRecord(scenario, archivedAt) {
        return {
            id: `history-${scenario.sceneLabel}-${archivedAt}`.replace(/[^a-zA-Z0-9-]/g, ""),
            source: "全程录音分析归档",
            archivedAt,
            ...scenario
        };
    }

    function initializeHistoryRecords() {
        historyRecords = initialHistoryEntries
            .map(entry => {
                const scenario = getScenarioByLabel(entry.sceneLabel);
                return scenario ? createHistoryRecord(scenario, entry.archivedAt) : null;
            })
            .filter(Boolean);
    }

    function archiveCurrentScenario() {
        if (!currentRecordingScenario) return null;

        const newRecord = createHistoryRecord(currentRecordingScenario, getNextArchiveTimestamp());
        historyRecords = [
            newRecord,
            ...historyRecords.filter(item => item.sceneLabel !== currentRecordingScenario.sceneLabel)
        ].slice(0, 6);

        return newRecord;
    }

    function hideEmptyState() {
        emptyState.style.display = "none";
    }

    function scrollToBottom() {
        requestAnimationFrame(() => {
            chatArea.scrollTop = chatArea.scrollHeight + 200;
        });
    }

    function addTextMessage(role, text) {
        hideEmptyState();
        const row = document.createElement("div");
        row.className = "message-row " + role;

        const bubble = document.createElement("div");
        bubble.className = "bubble " + role;
        bubble.innerHTML = text;

        row.appendChild(bubble);
        messageList.appendChild(row);
        scrollToBottom();
    }

    function addCardMessage(html) {
        hideEmptyState();
        const row = document.createElement("div");
        row.className = "message-row assistant";

        const cardWrap = document.createElement("div");
        cardWrap.className = "card-wrap";
        cardWrap.innerHTML = html;

        row.appendChild(cardWrap);
        messageList.appendChild(row);
        scrollToBottom();
    }

    function runAction(actionKey) {
        const item = presetData[actionKey];
        if (!item) return;

        addTextMessage("user", item.user);

        setTimeout(() => {
            addTextMessage("assistant", item.assistant);
        }, 280);

        setTimeout(() => {
            addCardMessage(item.card);
        }, 520);
    }

    function buildStatusCard(scenario, options) {
        const stoppedClass = options.stopped ? "status-pill stopped" : "status-pill";
        const durationRow = options.hideDuration ? "" : `<div class="service-label">录音时长</div><div class="service-value">${scenario.duration}</div>`;
        return `
            <div class="info-card">
                <div class="status-card-top">
                    <div>
                        <div class="card-title">${options.title}</div>
                        <div class="card-desc">${options.description}</div>
                    </div>
                    <div class="${stoppedClass}">
                        <span class="record-dot"></span>
                        ${options.status}
                    </div>
                </div>
                <div class="service-grid">
                    <div class="service-label">服务对象</div><div class="service-value">${scenario.resident}</div>
                    <div class="service-label">床位</div><div class="service-value">${scenario.bed}</div>
                    <div class="service-label">服务项目</div><div class="service-value">${scenario.service}</div>
                    <div class="service-label">执行护工</div><div class="service-value">${scenario.worker}</div>
                    ${durationRow}
                </div>
                ${options.note ? `<div class="recording-note">${options.note}</div>` : ""}
            </div>
        `;
    }

    function buildTagRow(tags) {
        return tags.map(tag => `<span class="tag tag-${tag.tone}">${tag.text}</span>`).join("");
    }

    function buildWaveBarsMarkup(mode) {
        const totalBars = 24;
        return Array.from({ length: totalBars }, (_, index) => {
            const activeClass = mode === "playback" && index < 10 ? " active" : "";
            const delay = (index % 6) * 0.12;
            return `<span class="wave-bar${activeClass}" style="animation-delay:${delay}s"></span>`;
        }).join("");
    }

    function buildArchiveCard(record) {
        return `
            <button class="archive-card" type="button" data-record-id="${record.id}">
                <div class="archive-card-top">
                    <div class="archive-card-main">
                        <div class="archive-name">${record.resident}</div>
                        <div class="archive-service">${record.service}</div>
                    </div>
                    <div class="archive-time">${record.archivedAt}</div>
                </div>
                <div class="archive-status-row">
                    <span class="archive-status-pill ${record.tone}">${record.satisfaction}</span>
                    <span class="archive-scene">${record.sceneLabel}</span>
                </div>
                <div class="archive-summary">${record.summary}</div>
                <div class="tag-row">${buildTagRow(record.tags)}</div>
                <div class="archive-meta-note">点击查看完整对话、标签建议与处理建议</div>
            </button>
        `;
    }

    function buildTranscriptLinesMarkup(transcript, count, extraClass) {
        return transcript.slice(0, count).map(item => `
            <div class="transcript-line ${extraClass || ""}">
                <span class="transcript-speaker">${item.speaker}</span>
                <div class="transcript-text">${item.text}</div>
            </div>
        `).join("");
    }

    function buildTranscriptCard(scenario) {
        const items = buildTranscriptLinesMarkup(scenario.transcript, scenario.transcript.length, "");

        return `
            <div class="info-card">
                <div class="card-title">完整对话内容</div>
                <div class="card-desc">以下内容为本次服务过程的完整对话整理结果。</div>
                <div class="transcript-list">${items}</div>
            </div>
        `;
    }

    function buildLiveAudioCard(scenario, options = {}) {
        const stopped = Boolean(options.stopped);
        const title = options.title || (stopped ? "录音已结束" : "录音采集中");
        const description = options.description || (stopped
            ? "本次服务录音已结束，系统正在整理并转写对话内容。"
            : "系统正在持续采集本次服务对话，结束录音后可发起转写。");
        const status = options.status || (stopped ? "已结束" : "录音中");
        const statusClass = stopped ? "status-pill stopped" : "status-pill";
        const timeText = options.timeText || (stopped ? scenario.duration : scenario.startTime);
        const waveStoppedClass = stopped ? " stopped" : "";

        return `
            <div class="info-card live-audio-card">
                <div class="live-audio-row">
                    <div class="audio-main">
                        <div class="audio-main-title">${title}</div>
                        <div class="audio-main-desc">${description}</div>
                    </div>
                    <div class="${statusClass}">
                        <span class="record-dot"></span>
                        ${status}
                    </div>
                </div>
                <div class="audio-wave-shell">
                    <div class="audio-wave-top">
                        <span class="audio-wave-label">服务录音流</span>
                        <span class="audio-wave-time">${timeText}</span>
                    </div>
                    <div class="audio-wave-track">
                        <div class="audio-wave-bg"></div>
                        <div id="liveWaveBars" class="wave-bars live${waveStoppedClass}">${buildWaveBarsMarkup("live")}</div>
                    </div>
                </div>
            </div>
        `;
    }

    function buildTranscribeAction() {
        return `
            <div class="inline-action-wrap">
                <button id="transcribeBtn" class="inline-action-btn" type="button">结束录音并转写</button>
            </div>
        `;
    }

    function buildStreamingCard() {
        return `
            <div class="info-card stream-card">
                <div class="card-title">对话转写内容</div>
                <div class="card-desc">下方内容将在结束录音后逐句流式输出，并作为生成 AI 分析的依据。</div>
                <div id="streamingTranscriptList" class="transcript-list streaming-list"></div>
            </div>
        `;
    }

    function buildPlaybackCard(scenario) {
        return `
            <div class="info-card playback-audio-card">
                <div class="card-title">录音回放</div>
                <div class="card-desc">以下为本次服务录音回放信息，可配合完整对话和 AI 建议查看完整内容。</div>
                <div class="playback-audio-row">
                    <div class="audio-main">
                        <div class="audio-wave-shell">
                            <div class="audio-wave-top">
                                <span class="audio-wave-label">服务录音文件</span>
                                <span class="audio-wave-time">${scenario.duration}</span>
                            </div>
                            <div class="audio-wave-track">
                                <div class="audio-wave-bg"></div>
                                <div class="audio-wave-progress"></div>
                                <div class="wave-bars playback">${buildWaveBarsMarkup("playback")}</div>
                            </div>
                        </div>
                    </div>
                    <button class="play-btn" type="button" aria-label="播放录音" aria-pressed="false">▶</button>
                </div>
            </div>
        `;
    }

    function buildAnalysisCard(scenario, options = {}) {
        const titleContent = options.showEditButton
            ? `
                <div class="card-title-row">
                    <div class="card-title">AI建议分析</div>
                    <button class="edit-btn" type="button">编辑</button>
                </div>
            `
            : `<div class="card-title">AI建议分析</div>`;

        return `
            <div class="info-card">
                ${titleContent}
                <div class="analysis-summary tone-${scenario.tone}">${scenario.banner}</div>
                <div class="analysis-grid">
                    <div class="analysis-label">服务对象</div><div class="analysis-value">${scenario.resident}</div>
                    <div class="analysis-label">床位</div><div class="analysis-value">${scenario.bed}</div>
                    <div class="analysis-label">服务项目</div><div class="analysis-value">${scenario.service}</div>
                    <div class="analysis-label">执行护工</div><div class="analysis-value">${scenario.worker}</div>
                    <div class="analysis-label">开始时间</div><div class="analysis-value">${scenario.startTime}</div>
                    <div class="analysis-label">结束时间</div><div class="analysis-value">${scenario.endTime}</div>
                    <div class="analysis-label">录音时长</div><div class="analysis-value">${scenario.duration}</div>
                    <div class="analysis-label">对话摘要</div><div class="analysis-value">${scenario.summary}</div>
                    <div class="analysis-label">关键反馈</div><div class="analysis-value">${scenario.keyFeedback}</div>
                    <div class="analysis-label">满意度判断</div><div class="analysis-value">${scenario.satisfaction}</div>
                    <div class="analysis-label">服务结论</div><div class="analysis-value">${scenario.conclusion}</div>
                    <div class="analysis-label">处理建议</div><div class="analysis-value">${scenario.suggestion}</div>
                </div>
                <div class="tag-row">${buildTagRow(scenario.tags)}</div>
            </div>
        `;
    }

    function renderStreamingTranscript() {
        const streamContainer = document.getElementById("streamingTranscriptList");
        if (!streamContainer || !currentRecordingScenario) return;

        if (streamedTranscriptCount === 0) {
            streamContainer.innerHTML = `
                <div class="stream-placeholder">
                    正在转写本次服务对话内容，识别结果将逐句显示。
                </div>
            `;
            return;
        }

        streamContainer.innerHTML = buildTranscriptLinesMarkup(
            currentRecordingScenario.transcript,
            streamedTranscriptCount,
            "stream-line"
        );
    }

    function setLiveWaveRunning(isRunning) {
        const liveWaveBars = document.getElementById("liveWaveBars");
        if (!liveWaveBars) return;

        liveWaveBars.classList.toggle("stopped", !isRunning);
    }

    function clearTranscriptStream() {
        if (transcriptStreamTimer) {
            clearTimeout(transcriptStreamTimer);
            transcriptStreamTimer = null;
        }
    }

    function scheduleTranscriptStep(delay) {
        transcriptStreamTimer = setTimeout(() => {
            if (!currentRecordingScenario || recordingAnalyzed) {
                transcriptStreamTimer = null;
                return;
            }

            if (streamedTranscriptCount < currentRecordingScenario.transcript.length) {
                streamedTranscriptCount += 1;
                renderStreamingTranscript();
                scheduleTranscriptStep(860);
                return;
            }

            transcriptCompleted = true;
            analyzeBtn.disabled = false;
            setLiveWaveRunning(false);
            transcriptStreamTimer = null;
        }, delay);
    }

    function startTranscriptStream() {
        clearTranscriptStream();
        streamedTranscriptCount = 0;
        transcriptCompleted = false;
        renderStreamingTranscript();
        scheduleTranscriptStep(360);
    }

    function bindDemoPlayButtons(container) {
        if (!container) return;

        container.querySelectorAll(".play-btn").forEach(button => {
            button.addEventListener("click", () => {
                const currentCard = button.closest(".playback-audio-card");
                const isPlaying = button.getAttribute("aria-pressed") === "true";

                container.querySelectorAll(".playback-audio-card.is-playing").forEach(card => {
                    if (card !== currentCard) {
                        card.classList.remove("is-playing");
                        const otherButton = card.querySelector(".play-btn");
                        if (otherButton) {
                            otherButton.setAttribute("aria-pressed", "false");
                            otherButton.textContent = "▶";
                        }
                    }
                });

                if (currentCard) {
                    currentCard.classList.toggle("is-playing", !isPlaying);
                }

                button.setAttribute("aria-pressed", isPlaying ? "false" : "true");
                button.textContent = isPlaying ? "▶" : "❚❚";
            });
        });
    }

    function renderRecordingLanding() {
        if (!currentRecordingScenario) return;

        recordingContent.innerHTML = `
            ${buildLiveAudioCard(currentRecordingScenario)}
            ${buildTranscribeAction()}
        `;

        bindRecordingActionButtons();
    }

    function renderRecordingTranscribing() {
        if (!currentRecordingScenario) return;

        recordingContent.innerHTML = `
            ${buildLiveAudioCard(currentRecordingScenario, {
                stopped: true,
                status: "转写中",
                timeText: currentRecordingScenario.duration
            })}
            ${buildStreamingCard()}
        `;

        renderStreamingTranscript();
    }

    function renderAnalyzingState() {
        if (!currentRecordingScenario) return;

        recordingContent.innerHTML = `
            ${buildStatusCard(currentRecordingScenario, {
                title: "录音已结束",
                description: "本次服务录音已结束，系统正在生成分析结果并整理服务建议。",
                status: "分析中",
                stopped: true
            })}
            <div class="info-card">
                <div class="loading-card">
                    <div class="loading-spinner"></div>
                    <div>
                        <div class="card-title">正在生成 AI 分析</div>
                        <div class="card-desc">请稍候，系统将基于本次录音转写内容生成服务建议与分析结果。</div>
                    </div>
                </div>
            </div>
        `;
    }

    function renderRecordingResult() {
        if (!currentRecordingScenario) return;

        recordingContent.innerHTML = `
            ${buildAnalysisCard(currentRecordingScenario, { showEditButton: true })}
        `;
    }

    function renderHistoryList() {
        historyListContent.innerHTML = `
            <div class="recording-hero">
                <div class="scene-badge">已归档 ${historyRecords.length} 条</div>
                <div class="recording-hero-desc">可查看全程录音分析后的服务归档，点击任意记录进入详情页查看完整内容。</div>
            </div>
            <div class="recording-stack">
                <div class="info-card">
                    <div class="card-title">最近服务归档</div>
                    <div class="card-desc">以下记录覆盖满意、不满意与轻微不适等典型服务场景。</div>
                </div>
                <div class="archive-list">
                    ${historyRecords.map(buildArchiveCard).join("")}
                </div>
            </div>
        `;

        historyListContent.querySelectorAll(".archive-card").forEach(card => {
            card.addEventListener("click", () => {
                const targetId = card.getAttribute("data-record-id");
                const record = historyRecords.find(item => item.id === targetId);
                if (record) {
                    openHistoryDetail(record);
                }
            });
        });
    }

    function renderHistoryDetail() {
        if (!currentHistoryRecord) return;

        historyDetailContent.innerHTML = `
            <div class="recording-hero">
                <div class="scene-badge">${currentHistoryRecord.sceneLabel}</div>
                <div class="recording-hero-desc">查看本次服务的归档信息、完整对话内容与分析建议。</div>
            </div>
            <div class="recording-stack">
                ${buildAnalysisCard(currentHistoryRecord)}
                ${buildPlaybackCard(currentHistoryRecord)}
                ${buildTranscriptCard(currentHistoryRecord)}
            </div>
        `;

        bindDemoPlayButtons(historyDetailContent);
    }

    function bindRecordingActionButtons() {
        const transcribeBtn = document.getElementById("transcribeBtn");
        if (!transcribeBtn) return;

        transcribeBtn.addEventListener("click", handleTranscribeClick);
    }

    function handleTranscribeClick() {
        if (!currentRecordingScenario || transcriptStarted || recordingAnalyzed) return;

        transcriptStarted = true;
        analyzeBtn.disabled = true;
        renderRecordingTranscribing();
        startTranscriptStream();
    }

    function openRecordingDemo() {
        currentRecordingScenario = recordingScenarios[recordingScenarioIndex % recordingScenarios.length];
        recordingScenarioIndex += 1;
        recordingAnalyzed = false;
        streamedTranscriptCount = 0;
        transcriptStarted = false;
        transcriptCompleted = false;

        if (analyzingTimer) {
            clearTimeout(analyzingTimer);
            analyzingTimer = null;
        }

        clearTranscriptStream();
        analyzeBtn.textContent = "生成AI分析";
        analyzeBtn.disabled = true;
        showView(recordingView, RECORDING_TOP);
        renderRecordingLanding();
    }

    function closeRecordingDemo() {
        if (analyzingTimer) {
            clearTimeout(analyzingTimer);
            analyzingTimer = null;
        }

        clearTranscriptStream();
        recordingAnalyzed = false;
        transcriptStarted = false;
        transcriptCompleted = false;
        showView(mainView, DEFAULT_TOP);
    }

    function openHistoryList() {
        currentHistoryRecord = null;
        renderHistoryList();
        showView(historyListView, HISTORY_LIST_TOP);
    }

    function openHistoryDetail(record) {
        currentHistoryRecord = record;
        renderHistoryDetail();
        showView(historyDetailView, HISTORY_DETAIL_TOP);
    }

    function handleAnalyzeClick() {
        if (!currentRecordingScenario) return;

        if (recordingAnalyzed) {
            const record = archiveCurrentScenario();
            if (record) {
                openHistoryDetail(record);
            }
            return;
        }

        if (!transcriptStarted || !transcriptCompleted) return;

        clearTranscriptStream();
        analyzeBtn.disabled = true;
        setTopBar(ANALYSIS_TOP);
        renderAnalyzingState();

        analyzingTimer = setTimeout(() => {
            recordingAnalyzed = true;
            analyzeBtn.disabled = false;
            analyzeBtn.textContent = "提交";
            renderRecordingResult();
            analyzingTimer = null;
        }, 720);
    }

    function normalizeInput(text) {
        return text.replace(/\\s+/g, "");
    }

    function parseAction(text) {
        const q = normalizeInput(text);

        if (q.includes("AI智能服务") || q.includes("AI智能护理") || q.includes("全程录音") || q.includes("服务留痕") || q.includes("对话分析")) {
            return "full_record";
        }
        if (q.includes("历史服务记录") || q.includes("历史记录") || q.includes("服务归档")) {
            return "history_record";
        }
        if (q.includes("今日") && (q.includes("护理任务") || q.includes("任务"))) {
            return "task";
        }
        if (q.includes("床位")) {
            return "bed";
        }
        if (q.includes("待办") || q.includes("服务")) {
            return "todo";
        }
        if (q.includes("重点") || q.includes("关注对象")) {
            return "focus";
        }
        if (
            q.includes("喂药") ||
            q.includes("洗澡") ||
            q.includes("压疮护理") ||
            q.includes("翻身") ||
            q.includes("护理记录") ||
            q.includes("做了什么") ||
            q.includes("完成了什么")
        ) {
            return "care_record";
        }
        if (q.includes("王秀兰") || q.includes("基本情况") || q.includes("老人情况")) {
            return "profile";
        }
        return null;
    }

    function handleTextSend() {
        const value = textInput.value.trim();
        if (!value) return;

        const matchedAction = parseAction(value);
        textInput.value = "";

        if (matchedAction === "full_record") {
            openRecordingDemo();
            return;
        }

        if (matchedAction === "history_record") {
            openHistoryList();
            return;
        }

        if (matchedAction) {
            addTextMessage("user", value);

            setTimeout(() => {
                addTextMessage("assistant", presetData[matchedAction].assistant);
            }, 280);

            setTimeout(() => {
                addCardMessage(presetData[matchedAction].card);
            }, 520);
        } else {
            addTextMessage("user", value);

            setTimeout(() => {
                addTextMessage(
                    "assistant",
                    "您可以尝试输入：AI智能服务、历史服务记录、今日护理任务、王秀兰老人基本情况、查看床位清单、查询待办服务、重点关注对象。"
                );
            }, 280);
        }
    }

    initializeHistoryRecords();

    chipButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            const action = btn.getAttribute("data-action");

            if (action === "full_record") {
                openRecordingDemo();
                return;
            }

            runAction(action);
        });
    });

    voiceBtn.addEventListener("click", () => {
        const action = voiceSequence[voiceIndex % voiceSequence.length];
        voiceIndex += 1;
        runAction(action);
    });

    moreBtn.addEventListener("click", openMoreSheet);
    sheetOverlay.addEventListener("click", closeMoreSheet);
    fullRecordMenuBtn.addEventListener("click", () => {
        closeMoreSheet();
        openRecordingDemo();
    });
    historyMenuBtn.addEventListener("click", () => {
        closeMoreSheet();
        openHistoryList();
    });

    analyzeBtn.addEventListener("click", handleAnalyzeClick);
    historyListBackBtn.addEventListener("click", () => {
        showView(mainView, DEFAULT_TOP);
    });
    historyDetailBackBtn.addEventListener("click", () => {
        openHistoryList();
    });
    historyDetailHomeBtn.addEventListener("click", () => {
        showView(mainView, DEFAULT_TOP);
    });

    textInput.addEventListener("keydown", (e) => {
        if (e.key === "Enter") {
            e.preventDefault();
            handleTextSend();
        }
    });
</script>
</body>
</html>
"""

components.html(phone_html, height=830, scrolling=False)
