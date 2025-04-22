// GitHub Profile Renderer - Client-side only version
document.addEventListener('DOMContentLoaded', function() {
    // Process all GitHub handles in the document
    function processGitHubHandles() {
        // Find all elements that might contain GitHub handles
        const elements = document.querySelectorAll('p, li, h1, h2, h3, h4, h5, h6, blockquote');
        
        elements.forEach(function(element) {
            const text = element.innerHTML;
            if (!text) return;
            
            // Pattern to find GitHub handles
            const pattern = /@([a-zA-Z0-9-]+)\b/g;
            let match;
            const handles = [];
            
            // Find all GitHub handles in the text
            while ((match = pattern.exec(text)) !== null) {
                handles.push({
                    username: match[1],
                    startPos: match.index,
                    endPos: match.index + match[0].length
                });
            }
            
            if (handles.length === 0) return;
            
            // Handle special case for Bonsai guide
            if (element.tagName === 'BLOCKQUOTE' && element.textContent.includes('@jsiegle')) {
                // Special handling for the Bonsai guide author
                const username = 'jsiegle'; // Known username from the text
                
                // Create a profile card directly after the blockquote
                const card = document.createElement('div');
                card.className = 'github-profile-card';
                card.style.maxWidth = '300px';
                card.style.margin = '20px 0';
                
                // Display a static profile card without API call
                displayStaticProfile(username, card);
                
                // Insert the card after the blockquote
                element.parentNode.insertBefore(card, element.nextSibling);
                return; // Skip regular processing for this element
            }
            
            // Create a profiles row for this element
            const profilesRow = document.createElement('div');
            profilesRow.className = 'github-profiles-row';
            
            // Create a profile card for each handle
            handles.forEach(function(handle) {
                const card = document.createElement('div');
                card.className = 'github-profile-card';
                
                // Display a static profile without API call
                displayStaticProfile(handle.username, card);
                
                profilesRow.appendChild(card);
            });
            
            // Insert the profiles row after the element
            element.parentNode.insertBefore(profilesRow, element.nextSibling);
        });
    }
    
    // Display a static profile without API calls
    function displayStaticProfile(username, cardContainer) {
        // Create profile card without GitHub API data
        cardContainer.innerHTML = `
            <div class="profile-card">
                <div class="profile-image">
                    <a href="https://github.com/${username}" target="_blank">
                        <div class="profile-avatar-placeholder">${username.charAt(0).toUpperCase()}</div>
                    </a>
                </div>
                <div class="profile-info">
                    <h4><a href="https://github.com/${username}" target="_blank">${username}</a></h4>
                    <p class="username">@${username}</p>
                </div>
            </div>
        `;
    }
    
    // Fetch and display a GitHub profile - Not currently used due to API limitations
    function fetchAndDisplayProfile(username, cardContainer) {
        const headers = {
            'Accept': 'application/vnd.github.v3+json'
        };
        
        fetch(`https://api.github.com/users/${username}`, { headers })
            .then(response => {
                if (response.status === 403) {
                    console.warn('GitHub API rate limit exceeded - falling back to static display');
                    throw new Error('GitHub API rate limit exceeded');
                }
                if (!response.ok) {
                    throw new Error('GitHub profile not found');
                }
                return response.json();
            })
            .then(data => {
                // Create profile card with GitHub data
                const displayName = data.name || username;
                
                cardContainer.innerHTML = `
                    <div class="profile-card">
                        <div class="profile-image">
                            <a href="${data.html_url}" target="_blank">
                                <img src="${data.avatar_url}" alt="${displayName}'s avatar">
                            </a>
                        </div>
                        <div class="profile-info">
                            <h4><a href="${data.html_url}" target="_blank">${displayName}</a></h4>
                            <p class="username">@${username}</p>
                            ${data.bio ? `<p class="bio">${data.bio}</p>` : ''}
                        </div>
                    </div>
                `;
            })
            .catch(error => {
                // If fetching fails, display static profile
                displayStaticProfile(username, cardContainer);
                console.error('Error fetching GitHub profile:', error);
            });
    }
    
    // Add CSS for GitHub profiles
    const style = document.createElement('style');
    style.textContent = `
        .github-profiles-row {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 10px 0;
        }
        .github-profile-card {
            flex: 1 1 250px;
            min-width: 200px;
            max-width: 300px;
            margin: 5px 0;
        }
        .profile-card {
            display: flex;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 10px;
            background-color: #f6f8fa;
        }
        .profile-image img {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            margin-right: 10px;
        }
        .profile-avatar-placeholder {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            margin-right: 10px;
            background-color: #0366d6;
            color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            font-weight: bold;
        }
        .profile-info h4 {
            margin: 0 0 5px 0;
            font-size: 0.95em;
        }
        .profile-info .username {
            margin: 0 0 5px 0;
            font-size: 0.8em;
            color: #586069;
        }
        .profile-info .bio {
            margin: 5px 0 0 0;
            font-size: 0.85em;
            color: #586069;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
            text-overflow: ellipsis;
        }
        .loading {
            font-style: italic;
            color: #586069;
            font-size: 0.9em;
        }
    `;
    document.head.appendChild(style);
    
    // Run processor
    processGitHubHandles();
});