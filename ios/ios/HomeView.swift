//
//  HomeView.swift
//  ios
//
//  Created by Sophia Xu on 2026-01-17.
//

import SwiftUI

struct HomeView: View {
    var body: some View {
        Menu("Voice Picker") {
            Button("Default", action: sendVoice)
            Button("Default", action: sendVoice)
            Button("Default", action: sendVoice)
            Button("Default", action: sendVoice)
            Button("Default", action: sendVoice)
        }
    }
    func sendVoice() {
        // call endpoint here
        
    }
}


