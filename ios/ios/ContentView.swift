//
//  ContentView.swift
//  ios
//
//  Created by Ethan Parker Wong on 2026-01-17.
//

import SwiftUI

struct ContentView: View {
    var body: some View {
        NavigationStack {
            ZStack {
                BackgroundView(videoName: "spacebackground", videoType: "mov")
                    .ignoresSafeArea()
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                    .allowsHitTesting(false)
    //            Image(systemName: "globe")
    //                .imageScale(.large)
    //                .foregroundStyle(.tint)
                Text("labubuly")
                    .foregroundColor(.white)
                    .font(.system(size: 40, weight: .bold, design: .rounded))
                
                NavigationLink("Enter") {
                    HomeView()
                }

                
            }
            
        }
        
        //.padding()
    }
}

#Preview {
    ContentView()
}
